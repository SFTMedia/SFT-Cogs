from redbot.core import commands

class BlueXD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    __version__ = "1.1.0"

    @commands.command()
    async def blue(self,ctx):
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
