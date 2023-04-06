import asyncio
import configparser
import discord
from valve.source.a2s import ServerQuerier, NoResponseError
from a2s import NoResponseError, ServerQuerier
import a2s
from valve.rcon import RCON, AuthenticationError

from datetime import datetime
from discord.ext import commands, tasks

config = configparser.ConfigParser()
config.read('config.ini')

class ValheimBridge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #self.server_process = None
        self.server_ip = config.get('Server', 'server_ip')
        self.server_port = int(config.get('Server', 'server_port'))
        self.rcon_password = config.get('Server', 'rcon_password')
        self.channel_id = int(config.get('Discord', 'channel_id'))
        #self.server = valve.source.a2s.ServerQuerier((self.server_ip, self.server_port), timeout=5)
        self.server = a2s.valve.source.a2s.ServerQuerier((self.server_ip, self.server_port))
        self.event_start_time = None
        self.command_prefix = config.get('Discord', 'command_prefix')
        self.admin_role_names = config.get('Discord', 'admin_role_names').split(',')
        self.server_status_message_id = None
        self.server_status_message = None
        self.server_status = False
        self.playerlist = []
        self.event_task = None
        
        self.event_task = asyncio.create_task(self.check_player_changes())
        self.event_task = asyncio.create_task(self.check_events())
        self.event_task = asyncio.create_task(self.check_player_deaths())

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

        # Initialize A2S and RCON instances
        self.a2s = a2s.A2SInfo(self.server_ip, self.server_port)
        self.rcon = RCON(self.server_ip, self.rcon_password)

        # Connect to Discord channel
        self.channel = self.get_channel(self.channel_id)

        # Send message to Discord channel when bot is ready
        await self.channel.send('Server bridge is now online!')   

    def cog_unload(self):
        asyncio.create_task(self.cancel_tasks())

    async def rcon_command(self, command: str) -> str:
        try:
            with a2s.Rcon(self.server_ip, self.rcon_password, self.server_port) as rcon:
                response = await rcon.execute(command)
                return response
        except a2s.BrokenMessageError:
            return "Error: Received a broken message from the server"
        except a2s.RconError as e:
            #self.channel.send(f"Could not connect to server")
            #return None
            return f"Error: {str(e)}"

    async def check_player_changes(self):
        global player_list
        global server_online

        while True:
            try:
                with self.valve.source.a2s.ServerQuerier((self.server_ip, self.server_port)) as server:
                    server_info = server.info()
                    if not server_online:
                        server_online = True
                        await self.get_channel(int(config.get('Discord', 'channel_id'))).send(f"Server {server_info['server_name']} is now online!")
                    new_player_list = server.players()['players']
                    new_player_list_names = [player['name'] for player in new_player_list]
                    joiners = set(new_player_list_names) - set(player_list)
                    quitters = set(player_list) - set(new_player_list_names)
                    player_list = new_player_list_names
                    if joiners:
                        await self.get_channel(int(config.get('Discord', 'channel_id'))).send(f"Players joined: {', '.join(joiners)}")
                    if quitters:
                        await self.get_channel(int(config.get('Discord', 'channel_id'))).send(f"Players left: {', '.join(quitters)}")
            except self.valve.source.a2s.NoResponseError:
                if server_online:
                    server_online = False
                    await self.get_channel(int(config.get('Discord', 'channel_id'))).send("Server is now offline.")
                    player_list = []
        await asyncio.sleep(60)

    async def check_player_deaths(self):
        # Check death list
        try:
            death_list = await self.rcon.send_command('lodb')
        except a2s.RCONAuthenticationError:
            await self.channel.send('RCON password is incorrect.')
            return
        except a2s.RCONConnectionError:
            await self.channel.send('Failed to connect to RCON. Is the server running?')
            return
        death_list = death_list.strip().split('\n')[1:]
        current_deaths = [death.split(':')[0] for death in death_list]

        # Check for new deaths
        new_deaths = set(current_deaths) - set(self.last_deaths)
        for death in new_deaths:
            cause = death.split(' - ')[-1]
            await self.channel.send(f'{death} died from {cause}!')

        # Update last deaths
        self.last_deaths = current_deaths

    async def check_events(self):
        # Check event list
        try:
            event_list = await self.rcon.send_command('listevents')
        except a2s.RCONAuthenticationError:
            await self.channel.send('RCON password is incorrect.')
            return
        except a2s.RCONConnectionError:
            await self.channel.send('Failed to connect to RCON. Is the server running?')
            return
        event_list = event_list.strip().split('\n')[1:]
        current_events = [event.split(' ')[0] for event in event_list]

        # Check for new events
        new_events = set(current_events) - set(self.last_events)
        for event in new_events:
            await self.channel.send(f'{event} has started!')

        # Check for ended events
        ended_events = set(self.last_events) - set(current_events)
        for event in ended_events:
            await self.channel.send(f'{event} has ended.')

        # Update last events
        self.last_events = current_events

    @commands.Cog.listener()
    async def on_message(self, message):
        #if message.author == self.user:
        if message.author == self.bot.user:
            return
        if message.channel.id != self.channel_id:
            return
        if message.content.startswith(self.command_prefix):
            command = message.content[len(self.command_prefix):]
            try:
                if command == 'online':
                    status = await self.rcon_command('list')
                    if status:
                        await message.channel.send(status)
                    else:
                        await message.channel.send('Could not connect to server.')
                elif command == 'playerlist':
                    status = await self.rcon_command('list')
                    if status:
                        lines = status.split('\n')[1:]
                        if len(lines) == 1:
                            await message.channel.send('No players are currently online.')
                        else:
                            player_names = [line.split()[2] for line in lines if len(line.split()) > 2]
                            await message.channel.send(f'Players online ({len(player_names)}): {", ".join(player_names)}')
                    else:
                        await message.channel.send('Could not connect to server.')
                elif command == 'serverinfo':
                    info = self.server.get_info()
                    player_count = info.get("player_count")
                    max_players = info.get("max_players")
                    server_name = info.get("server_name")
                    map_name = info.get("map_name")
                    await message.channel.send(f"**{server_name}**\nMap: {map_name}\n{player_count}/{max_players} players online")
                elif command.startswith('kick '):
                    role_names = config.get('discord', 'admin_role_names').split(',')
                    admin_roles = [discord.utils.get(message.guild.roles, name=name) for name in role_names]
                    if not any(role in message.author.roles for role in admin_roles):
                        await message.channel.send('You do not have permission to use this command.')
                        return
                    args = command.split(' ')[1:]
                    if len(args) == 0:
                        await message.channel.send('Please specify a player to kick.')
                    else:
                        player_name = args[0]
                        #await a2s.rcon.command(f'kick {player_name}')
                        await self.server.rcon.command(f'kick {player_name}')
                        await message.channel.send(f'{player_name} has been kicked from the server.')
            except ConnectionError:
                await message.channel.send("Error: Could not connect to server.")
        else:
            try:
                self.server.rcon("say [Discord] {}: {}".format(message.author.name, message.content))
            except a2s.valve.source.NoResponseError:
                await message.channel.send("The server is not responding.")

    # Cancel all tasks when cog is unloaded
    async def cancel_tasks(self):
        if self.check_player_changes:
            self.check_player_changes.cancel()
        if self.check_events:
            self.check_events.cancel()
        if self.check_player_deaths:
            self.check_player_deaths.cancel()
        await self.channel.send('Server bridge is now offline.')
        
def setup(bot):
    bot.add_cog(ValheimBridge(bot))