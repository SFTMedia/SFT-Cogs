from redbot.core import commands

class Opinion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def opinion(self,ctx):
        """Posts a legal disclaimer"""

        opinion_message = (
            "For legal reasons, the above message is the sole personal opinion of the user who sent it and does NOT reflect the collective views of SFTMedia, Inc.")

        await ctx.send(opinion_message)


def setup(bot):
    n = Opinion(bot)
    bot.add_cog(n)