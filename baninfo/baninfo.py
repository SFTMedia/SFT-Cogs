from redbot.core import commands
from discord import User,NotFound,Forbidden
import datetime
class BanInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.deleted_messages=[]

    __version__ = "1.1.0"

    @commands.Cog.listener()
    async def on_raw_bulk_message_delete(self, payload):
        for message in payload.cached_messages:
            self.deleted_messages.append({"message":message,"cached_at":datetime.datetime.now()})

    @commands.command()
    async def baninfo(self, ctx, *, member: User):
        """Shows ban reason and any newly (last 36h) deleted messages due to a ban"""
        await ctx.send("Ban record for <@"+str(member.id)+">")
        try:
            ban_reason = await ctx.guild.fetch_ban(member)
            if ban_reason.reason!=None:
                await ctx.send("Ban was for "+str(ban_reason.reason))
            else:
                await ctx.send("No reason specified for the ban")
        except NotFound:
            await ctx.send("<@"+str(member.id)+"> is not banned, you can't see their deleted messages")
            return
        except Forbidden:
            await ctx.send("Missing ban members permission")
            return

        # Clear out old messages before the user can see them
        self.deleted_messages=[message for message in self.deleted_messages if message["cached_at"]+datetime.timedelta(hours=36) > datetime.datetime.now()] # change to 36h late

        for message in self.deleted_messages:
            if message["message"].author==member:
                await ctx.send("```"+message["message"].content+"``` in <#"+str(message["message"].channel.id)+"> at "+str(message["message"].created_at))

