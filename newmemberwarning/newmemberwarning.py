import discord
from discord.ext import commands
from redbot.core import Config, commands
from datetime import datetime, timedelta, timezone

class NewMemberWarning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        self.config.register_global(warning_channel_id=None)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user}')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Make datetime.utcnow() timezone-aware
        now_aware = datetime.utcnow().replace(tzinfo=timezone.utc)
        # Check if the account was created less than a week ago
        if (now_aware - member.created_at) < timedelta(weeks=1):
            warning_channel_id = await self.config.warning_channel_id()
            warning_channel = self.bot.get_channel(warning_channel_id)
            if warning_channel:
                join_date = member.created_at.strftime("%Y-%m-%d %H:%M:%S %Z")
                await warning_channel.send(
                    f'User {member.name} joined, Discord join date: {join_date}'
                )

    @commands.command()
    @commands.admin_or_permissions(manage_guild=True)
    async def setwarningchannel(self, ctx, channel: discord.TextChannel):
        """Set the channel for new member warnings"""
        await self.config.warning_channel_id.set(channel.id)
        await ctx.send(f"Warning channel set to {channel.mention}")

def setup(bot):
    bot.add_cog(NewMemberWarning(bot))