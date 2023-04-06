import asyncio
import discord
from discord.ext import commands
import gamedig

class ValheimBridge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.valheim_ip = "rust.superfuntime.org" # Replace with your Valheim server IP
        self.valheim_port = 2456 # Replace with your Valheim server port
        self.valheim_rcon_password = "password" # Replace with your Valheim server RCON password
        self.discord_channel_id = 1092210477892898926 # Replace with the ID of the Discord channel to send messages to
        self.valheim_interval = 5 # The interval in seconds to check for new messages from Valheim
        self.valheim_last_message = ""

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

                valheim_messages = valheim_info["raw"]["chat"]
                if valheim_messages and valheim_messages[-1] != self.valheim_last_message:
                    self.valheim_last_message = valheim_messages[-1]
                    await self.send_to_discord(self.valheim_last_message)

            except asyncio.TimeoutError:
                pass

    async def send_to_discord(self, message):
        channel = await self.bot.fetch_channel(self.discord_channel_id)
        await channel.send(f"**Valheim:** {message}")

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.connect_to_valheim())

def setup(bot):
    bot.add_cog(ValheimBridge(bot))
