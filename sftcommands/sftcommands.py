from redbot.core import commands

class SFTCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def shop(self,ctx):
        """Links Discord Premium Shop"""

        discord_shop_msg = (
            "**Check out our Discord Premium Shop here** ->\n"
	        "https://superfuntime.buycraft.net/category/discord")

        await ctx.send(discord_shop_msg)


    @commands.command()
    async def mcshop(self,ctx):
        """Links Minecraft Premium Shop"""

        mc_shop_msg = (
            "**Check out our Server Premium Shop here** ->\n"
	        "https://www.superfuntime.org/shops")

        await ctx.send(mc_shop_msg)


    @commands.command()
    async def merchshop(self,ctx):
        """Links SFT Merch Shop"""

        merch_shop_msg = (
            "**Check out our Merch Shop here** ->\n"
            "https://shop.spreadshirt.com/superfuntime/")

        await ctx.send(merch_shop_msg)


    @commands.command()
    async def ip(self,ctx):
        """Links SFT server list"""

        server_list_msg = (
            "**Check out all the servers we host here** ->\n"
	        "https://www.superfuntime.org/forum/index.php/topic,89705.0.html")

        await ctx.send(server_list_msg)


    @commands.command()
    async def vote(self,ctx):
        """Links SFT vote sites"""

        vote_msg = (
            "**Vote for our servers here** ->\n"
	        "https://www.superfuntime.org/vote")

        await ctx.send(vote_msg)


    @commands.command()
    async def patreon(self,ctx):
        """Links SFT patreon"""

        vote_msg = (
            "**You can support us on Pateron and get unique perks and rewards (such as a shiny discord rank, premium shop credit, etc) and help the server from as low as $5 / mo\n"
	        "https://www.patreon.com/sftmedia")

        await ctx.send(patreon_msg)


def setup(bot):
    n = SFTCommands(bot)
    bot.add_cog(n)
