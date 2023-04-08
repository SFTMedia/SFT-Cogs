import discord
from discord.ext import commands, tasks
import valve.source.a2s
import valve.rcon

import configparser
import asyncio

class Valheim(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server_ip = ""
        self.server_port = 0
        self.rcon_password = ""
        self.channel_id = 0
        self.role_names = []
        self.last_playerlist = set()
        self.last_event = None
        self.playerlist_task = None
        self.event_task = None

        config = configparser.ConfigParser()
        config.read("config.ini")
        self.server_ip = config.get("server", "server_ip")
        self.server_port = config.getint("server", "server_port")
        self.rcon_password = config.get("server", "rcon_password")
        self.channel_id = config.getint("discord", "channel_id")
        self.role_names = config.get("discord", "role_names").split(",")

    async def cancel_tasks(self):
        if self.playerlist_task:
            self.playerlist_task.cancel()
        if self.event_task:
            self.event_task.cancel()

    def cog_unload(self):
        asyncio.create_task(self.cancel_tasks())

    async def check_player_changes(self):
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            with valve.source.a2s.ServerQuerier((self.server_ip, self.server_port)) as server:
                try:
                    info = server.info()
                    players = set(server.players()["players"])
                except valve.source.NoResponseError:
                    players = set()

            if players != self.last_playerlist:
                if players:
                    msg = f"Players online: {', '.join(players)}"
                else:
                    msg = "No players online"
                channel = self.bot.get_channel(self.channel_id)
                await channel.send(msg)

            self.last_playerlist = players
            await asyncio.sleep(30)

    async def check_events(self):
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            with valve.rcon.RCON((self.server_ip, self.server_port), self.rcon_password) as rcon:
                try:
                    response = rcon("listevents")
                    events = response.split("\n")[1:-1]
                except valve.rcon.RCONAuthenticationError:
                    events = []

            current_event = events[0] if events else None
            if current_event != self.last_event:
                if current_event:
                    msg = f"Event started: {current_event}"
                else:
                    msg = "Event stopped"
                channel = self.bot.get_channel(self.channel_id)
                await channel.send(msg)

            self.last_event = current_event
            await asyncio.sleep(30)

    @tasks.loop(minutes=1.0)
    async def update_playerlist(self):
        with valve.source.a2s.ServerQuerier((self.server_ip, self.server_port)) as server:
            try:
                info = server.info()
                players = set(server.players()["players"])
            except valve.source.NoResponseError:
                players = set()

        if players != self.last_playerlist:
            if players:
                msg = f"Players online: {', '.join(players)}"
            else:
                msg = "No players online"
            channel = self.bot.get_channel(self.channel_id)
            await channel.send(msg)

        self.last_playerlist = players

    @commands.Cog.listener()
    async def on_ready(self):
        print("Valheim cog is ready.")
        self.playerlist_task = asyncio.create_task(self.check_player_changes())
        self.event_task = asyncio.create_task(self