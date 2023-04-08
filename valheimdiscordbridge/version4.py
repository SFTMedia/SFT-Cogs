import asyncio
import configparser
import discord
from discord.ext import commands
from valve.source.a2s import ServerQuerier, NoResponseError


class ValheimBotCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server_ip = None
        self.server_port = None
        self.rcon_password = None
        self.channel_id = None
        self.role_names = None
        self.playerlist_task = None
        self.event_task = None
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    async def cancel_tasks(self):
        if self.playerlist_task:
            self.playerlist_task.cancel()
        if self.event_task:
            self.event_task.cancel()

    async def connect(self):
        try:
            server = (self.server_ip, self.server_port)
            with ServerQuerier(server) as query:
                return query
        except NoResponseError:
            return None

    async def check_player_changes(self):
        query = await self.connect()
        if query is None:
            return
        player_info = query.get_players()
        player_list = [player['name'] for player in player_info]
        channel = self.bot.get_channel(self.channel_id)
        async for message in channel.history():
            if message.author.bot:
                continue
            content = message.content
            if content.startswith(self.config['DEFAULT']['prefix'] + 'playerlist'):
                await message.edit(content=f"```{player_list}```")
        await asyncio.sleep(10)
        asyncio.create_task(self.check_player_changes())

    async def send_event_message(self, event):
        channel = self.bot.get_channel(self.channel_id)
        await channel.send(f"```{event}```")

    async def check_events(self):
        query = await self.connect()
        if query is None:
            return
        info = query.info()
        event = info.get('game', None)
        if event:
            if self.event != event:
                if self.event is not None:
                    await self.send_event_message(f'{self.event} ended.')
                self.event = event
                await self.send_event_message(f'{self.event} started.')
        else:
            if self.event is not None:
                await self.send_event_message(f'{self.event} ended.')
                self.event = None
        await asyncio.sleep(10)
        asyncio.create_task(self.check_events())

    @commands.Cog.listener()
    async def on_ready(self):
        self.server_ip = self.config['DEFAULT']['server_ip']
        self.server_port = int(self.config['DEFAULT']['server_port'])
        self.rcon_password = self.config['DEFAULT']['rcon_password']
        self.channel_id = int(self.config['DEFAULT']['channel_id'])
        self.role_names = [role_name.strip() for role_name in self.config['DEFAULT']['role_names'].split(',')]
        self.event = None
        asyncio.create_task(self.check_player_changes())
        asyncio.create_task(self.check_events())

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != self.channel_id:
            return
        if message.author.bot:
            return
        prefix = self.config['DEFAULT']['prefix']
        if message.content.startswith(prefix + 'playerlist'):
            query = await self.connect()
            if query is None:
                await message.channel.send('Server not responding.')
                return
            player_info = query.get_players()
            player_list = [player['name'] for player in player_info]
            await message.channel.send