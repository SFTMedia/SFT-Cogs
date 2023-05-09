from redbot.core import commands

class PCChecker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    __version__ = "1.1.0"

    @commands.command()
    async def sjw(self,ctx):
        """Lists SJW Rules"""

        sjw_rule = (
            "**SJW Rule:\n\n**"

            "This does not, in any way prevent people from being feminists / pro gay rights and so on. In fact this server is multi cultural, multi faith, multi gender and very socially acceptive towards everyone.\n"
            "It is still fine to be a feminist, gay rights defender, and so on. Just don't be \"in people's faces\" about that.\n\n"

            "Example of an appropriate thing to say:\n"
            "\"I think gay people should be allowed to get married\"\n"
            "\"I don't think gay people should be allowed to get married\"\n\n"

            "Example of a bad thing to say:\n"
            "\"I think gay people should be allowed to get married and if you don't agree with me you're a fucking moron\" \n"
            "\"I don't think gay people should be allowed to get married and if you don't agree with me you're a fucking moron\"\n\n"

            "I think we each need to allow everyone to have their own opinion on something and while we should try to get them to see that their opinion is wrong, we should not do that by being idiotic SJW's.\n\n"

            "NOTE: In my definition, SJW = person who forcibly imposes their beliefs on other people")

        #await ctx.send(sjw_rule)

        await ctx.send(sjw_rule)
