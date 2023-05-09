from redbot.core import commands

class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    __version__ = "1.1.0"


    @commands.command()
    async def quote(self,ctx):
        """Sends a random quote from a defined list"""
