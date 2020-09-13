from redbot.core import commands

class BlueXD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def blue(self):
        """Explains how Blue operates"""

        #blue_id = "<@140090865354932225>"

        blue_stuff = (
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n"
            "<@140090865354932225> sometimes makes bad decisions and sometimes they are stupid and/or also unfunny.\n")


        await ctx.send(blue_stuff)



def setup(bot):
    n = BlueXD(bot)
    bot.add_cog(n)
