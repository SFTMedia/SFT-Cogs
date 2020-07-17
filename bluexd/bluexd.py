from discord.ext import commands

class BlueXD:
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


        await self.bot.say(blue_stuff)



def setup(bot):
    n = BlueXD(bot)
    bot.add_cog(n)
