import asyncio
import configparser
import datetime
import discord
import logging
import os
import re
import valve.source.a2s
from redbot.core import commands.Cog


class ValheimBridge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server_ip = None
        self.server_port = None
        self.rcon_password = None
        self.channel_id = None
        self.role_names = []
        self.server = None
        self.server_info = None
        self.server_online = False
        self.player_list = []
        self.event_timer = None
        self.event_message_id = None
        self.event_message = None
        self.death_messages = {
            "was killed by": "was slain by",
            "was killed": "died",
            "was smacked": "was beaten to a pulp by",
            "fell to": "fell to their death",
            "was destroyed by the <color=": "was destroyed by the "
        }

    async def read_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.server_ip = config.get('Server', 'server_ip')
        self.server_port = config.getint('Server', 'server_port')
        self.rcon_password = config.get('Server', 'rcon_password')
        self.channel_id = config.getint('Discord', 'channel_id')
        self.role_names = config.get('Discord', 'role_names').split(',')

    async def connect_to_server(self):
        self.server = valve.source.a2s.ServerQuerier((self.server_ip, self.server_port))
        try:
            self.server_info = self.server.info()
        except valve.source.NoResponseError:
            logging.error('Could not connect to server')
            self.server_info = None

    async def check_player_changes(self):
        while True:
            try:
                new_player_list = self.server.players()['players']
                if set(new_player_list) != set(self.player_list):
                    if len(new_player_list) > len(self.player_list):
                        for player in new_player_list:
                            if player not in self.player_list:
                                await self.send_to_discord(f'**{player}** has joined the server!')
                    else:
                        for player in self.player_list:
                            if player not in new_player_list:
                                await self.send_to_discord(f'**{player}** has left the server.')
                    self.player_list = new_player_list
            except valve.source.NoResponseError:
                if self.server_online:
                    self.server_online = False
                    await self.send_to_discord('The server is offline.')
            else:
                if not self.server_online:
                    self.server_online = True
                    await self.send_to_discord('The server is online.')
            await asyncio.sleep(30)

    async def on_ready(self):
        logging.info(f'Logged in as {self.bot.user}')
        await self.read_config()
        await self.connect_to_server()
        self.event_timer = self.bot.loop.create_task(self.check_player_changes())

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != self.channel_id:
            return
        if not message.content.startswith(self.command_prefix):
            return
        command = message.content[len(self.command_prefix):].strip().lower()
        author_roles = [r.name.lower() for r in message.author.roles]
        if command.startswith("playerlist"):
            try:
                with A2SInfo(self.server) as info:
                    players = info.players()["players"]
                    if not players:
                        await self.send_to_discord("No one is currently playing on the server.")
                    else:
                        await self.send_to_discord(f"Players online: {' '.join(players)}")
            except A2SError:
                await self.send_to_discord("The server is currently offline.")
        elif command.startswith("kick "):
            if "kick" not in self.allowed_commands:
                await self.send_to_discord("Kicking players is not currently allowed.")
                return
            if not any(role in author_roles for role in self.allowed_roles):
                await self.send_to_discord("You do not have permission to use this command.")
                return
            try:
                name = command[len("kick "):].strip()
                with RCON(self.server, self.rcon_password) as rcon:
                    rcon.command(f"kick {name}")
                await self.send_to_discord(f"Kicked player: {name}")
            except RCONAuthenticationError:
                await self.send_to_discord("Invalid RCON password.")
            except RCONCommunicationError:
                await self.send_to_discord("Failed to communicate with the server.")
        else:
            await self.send_to_discord("Unknown command. Type +help for a list of commands.")
			
def setup(bot):
    bot.add_cog(ValheimBridge(bot))