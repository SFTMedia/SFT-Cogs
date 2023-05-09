from redbot.core import commands

class SFTCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    __version__ = "1.1.0"


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

        patreon_msg = (
            "You can support us on Pateron and get unique perks and rewards (such as a shiny discord rank, premium shop credit, etc) and help the server from as low as $5 / mo\n"
	        "https://www.patreon.com/sftmedia")

        await ctx.send(patreon_msg)


    @commands.command()
    async def faq(self,ctx):
        """Sends the SFT Discord FAQ message"""

        faq_msg = (
            "====[ Frequently Asked Questions ]====\n\n"
            "**What servers do we host?**\n"
            "You can view a full list of our servers here -> <https://www.superfuntime.org/forum/index.php/topic,89705.0.html>\n\n"
            "**Want to learn more about our community?**\n"
            "Check our our wiki here -> <https://wiki.superfuntime.org>\n\n"
            "**Need support?**\n"
            "Make a ticket by typing in #support\n\n"
            "**How do I rank up on discord?**\n"
            "Our ranks are handled by @Tatsu#8792 .  For every minute you send messages you earn xp and after a certain amount of do you rankup.  Rankup xp requirements are pinned in #bot-spam \n\n"
            "**Want notifications for updates on your favorite server?**\n"
            "Type `+selfrole` in #bot-spam and type the name of the rank you wish to receive\n\n"
            "**How can I send a message to ingame chat from discord?**\n"
            "All of our server chats are connected to discord channels.  You can talk to friends ingame and they can see your messages as well.  Head on over to #mc-network-chat \n\n"
            "**Have a server idea/bug to report?**\n"
            "Make a ticket by typing in #support \n\n"
            "**Want to join our serious topics/politics/religion channel?**\n"
            "Type `+selfrole add Insomniac` in #bot-spam \n\n"
            "**Want notifications for server updates and to be entered into our giveaways?**\n"
            "Type `+selfrole add Pingme` in #bot-spam \n\n"
            "**Want party game/jackbox notifications?**\n"
            "Type `+selfrole add PartyGamer` in #bot-spam \n\n"
            "**What are the rules for #insomniac-chat ?**\n"
            "All #rules apply besides discord etiquette rule #9.  Additionally, no sexual content or gore (as per discord ToS) and avoid overly edgy shock content please.\n\n"
            "**Unsure if something is against our rules here?**\n"
            "If you’re still unsure whether something not explicitly stated in #rules violates our rules or not, feel free to dm any member of our @Discord Admin team and we’d be happy to clarify! :)")

        await ctx.send(faq_msg)


    @commands.command()
    async def roles(self,ctx):
        """Sends information about the Discord donator roles"""

        roles_msg = (
            "====[ Discord Donator Roles ]====\n\n"
            "We now have 3 special Discord Donator ranks! @Discord Crab🦀 , @Discord Shark🦈 and @Discord Whale🐳 come with extra giveaway entries, 1 free custom emoji of your choice that you can change once per month, and a colored name ingame when you talk in #mc-network-chat !  These roles have just been added so more perks are likely to come in the future.\n\n"  
            "*NOTE: These are one time purchase roles, not subscription based.*\n\n"
            "You can purchase a rank here ->\n"
            "http://superfuntime.buycraft.net/category/discord")

        await ctx.send(roles_msg)
