from discord.ext import commands

class FindHelp:
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def findhelp(self):
        """Lists global crisis hotlines"""

        find_help_message = (
            "As a community we are always here to help and support each other and if you're having troubles with life you're always welcome to reach out to a friend or any of our staff members if you want advice or just need to vent and have someone to listen.  That being said, we are not experts so if you are in need of serious help with depression and/or self harm please seek professional care by visiting:\n\n" 

            "US: <https://www.thetrevorproject.org/> or <https://www.suicidepreventionlifeline.org/> , Call 1-866-488-7386 or 1-800-273-8255, or text HELP to 741741\n\n"

            "Europe: <https://www.iasp.info/resources/Crisis_Centres/Europe/> or <https://ibpf.org/resource/list-international-suicide-hotlines>\n\n"

            "Australia: <http://www.lifeline.org.au/> (Call 13-11-14), <https://www.beyondblue.org.au> (Call 1300-22-4636), or <https://kidshelpline.com.au> (Call 1800-55-1800)\n\n"

            "Other: <https://en.m.wikipedia.org/wiki/List_of_suicide_crisis_lines>")

        await self.bot.say(find_help_message)


def setup(bot):
    n = FindHelp(bot)
    bot.add_cog(n)
