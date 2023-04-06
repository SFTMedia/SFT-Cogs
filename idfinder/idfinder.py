from redbot.core import commands

class IDFinder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def idfinder(self,ctx):
        """Shows your User ID"""

        await ctx.send("Your Discord ID is `"+str(ctx.author.id)+"`")


def setup(bot):
    n = IDFinder(bot)
    bot.add_cog(n)
