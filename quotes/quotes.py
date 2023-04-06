from redbot.core import commands

class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def quote(self,ctx):
        """Sends a random quote from a defined list"""
        
        
        
        
        
        
def setup(bot):
    n = Quotes(bot)
    bot.add_cog(n)
