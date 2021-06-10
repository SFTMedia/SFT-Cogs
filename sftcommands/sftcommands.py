from redbot.core import commands

class SFTCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def shop(self,ctx):
        """Links Discord Premium Shop"""

        discord_shop_msg = (
            "Check out our Discord Premium Shop here ->\n"
			"https://super-fun-time-discord.tebex.io/")

        await ctx.send(discord_shop_msg)


    @commands.command()
    async def mcshop(self,ctx):
        """Links Minecraft Premium Shop"""

        mc_shop_msg = (
            "Check out our Discord Premium Shop here ->\n"
			"https://super-fun-time-discord.tebex.io/")

        await ctx.send(mc_shop_msg)


    @commands.command()
    async def ip(self,ctx):
        """Links SFT server list"""

        server_list_msg = (
            "Check out all the servers we host here ->\n"
			"https://www.superfuntime.org/forum/index.php/topic,89705.0.html")

        await ctx.send(server_list_msg)

def setup(bot):
    n = SFTCommands(bot)
    bot.add_cog(n)
