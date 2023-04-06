import asyncio
import discord
from discord.ext import commands
import gamedig
import a2s

class ValheimBridge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.valheim_ip = "127.0.0.1" # Replace with your Valheim server IP
        self.valheim_port = 2456 # Replace with your Valheim server port
        self.valheim_rcon_password = "password" # Replace with your Valheim server RCON password
        self.discord_channel_id = 1234567890 # Replace with the ID of the Discord channel to send messages to
        self.valheim_interval = 5 # The interval in seconds to check for new messages from Valheim
        self.valheim_last_message = ""
        self.valheim_last_players = []
        self.valheim_last_status = None

    async def connect_to_valheim(self):
        while True:
            try:
                valheim_info = await asyncio.wait_for(
                    loop.run_in_executor(None, gamedig.query, "valheim", {
                        "type": "valheim",
                        "host": self.valheim_ip,
                        "port": self.valheim_port,
                        "rconPassword": self.valheim_rcon_password
                    }), timeout=self.valheim_interval)

                # Check for server status
                valheim_status = valheim_info["raw"]["status"]
                if valheim_status != self.valheim_last_status:
                    if valheim_status == "running":
                        await self.send_to_discord("**Valheim:** Server started.")
                    elif valheim_status == "stopped":
                        await self.send_to_discord("**Valheim:** Server stopped.")

                    self.valheim_last_status = valheim_status

                # Check for new chat messages
                valheim_messages = valheim_info["raw"]["chat"]
                if valheim_messages and valheim_messages[-1] != self.valheim_last_message:
                    self.valheim_last_message = valheim_messages[-1]
                    await self.send_to_discord(f"**Valheim:** {self.valheim_last_message}")

                # Check for player death messages
                if "was killed by" in self.valheim_last_message:
                    death_message_parts = self.valheim_last_message.split()
                    player_name = death_message_parts[0]
                    death_cause = ' '.join(death_message_parts[3:])
                    await self.send_to_discord(f"**Valheim:** {player_name} died due to {death_cause}.")

                # Check for new players
                valheim_players = valheim_info["raw"]["players"]
                if valheim_players != self.valheim_last_players:
                    if len(valheim_players) > len(self.valheim_last_players):
                        new_players = list(set(valheim_players) - set(self.valheim_last_players))
                        await self.send_to_discord(f"**Valheim:** {' '.join(new_players)} joined the server.")
                    elif len(valheim_players) < len(self.valheim_last_players):
                        left_players = list(set(self.valheim_last_players) - set(valheim_players))
                        await self.send_to_discord(f"**Valheim:** {' '.join(left_players)} left the server.")

                    self.valheim_last_players = valheim_players

            except asyncio.TimeoutError:
                pass

    async def send_to_discord(self, message):
        channel = await self.bot.fetch_channel(self.discord_channel_id)

        if message == "+playerlist":
            valheim_info = await asyncio.wait_for(
                loop.run_in_executor(None, gamedig.query, "valheim", {
                    "type": "valheim",
                    "host": self.valheim_ip,
                    "port": self.valheim_port
                }), timeout=5)
            player_list = valheim_info["players"]
            if len(player_list) == 0:
                await channel.send("There are no players online.")
            else:
                players = "\n".join(player["name"] for player in player_list)
                await channel.send(f"Online players:\n{players}")
        else:
            await channel.send(message)

        # Send message back to Valheim chat if it was not sent by the Discord bot and not a player list request
        if message.author != self.bot.user and message != "+playerlist":
            rcon_message = f'say "{message.content}"'
            self.valheim_rcon.connect()
            self.valheim_rcon.execute(rcon_message)
            self.valheim_rcon.disconnect()

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.connect_to_valheim())

def setup(bot):
    bot.add_cog(ValheimBridge(bot))
