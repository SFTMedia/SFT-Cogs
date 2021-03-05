import datetime
from datetime import datetime
import time
from time import gmtime, strftime
from collections import namedtuple
from copy import deepcopy
import aiohttp
import asyncio
import urllib3
import re
import os
from redbot.core import commands


def setup(bot):
    bot.add_cog(SFTPlayerStats(bot))

class SFTPlayerStats(commands.Cog):
    """Cog that enables checking a users' ingame stats from discord!"""

    def __init__(self, bot):
        self.bot = bot

#self.defaultservers = DefaultServers(bot, "data/sftplayerstats/defaultservers.json")
        # self.file_path = "data/sftplayerstats/settings.json"
        # self.settings = dataIO.load_json(file_path)

    #@commands.group(name="defaultserver" pass_context=True)
    #async def setdefaultserver(self, ctx):
    #    """Set your default server to pull stats from!"""
    #    if ctx.invoked_subcommand is None:
    #        await send_cmd_helpt(ctx)

    #@defaultserver.command(pass_context=True, no_pm=True)
    #async def survival(self, ctx):
    #    """Check Survival uptime by default when \"+pstats\" is used"""
    #    settings = self.settings[ctx.messages.server.id]

    @commands.command()
    async def pstats(self, ctx, usertosearch : str,servertosearch:str=None):
        """States the given users' ingame uptime\n"""
        if not servertosearch:
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=MAIN&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "survival" or servertosearch == "Survival"): # Survival
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=MAIN&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "creative" or servertosearch == "Creative"): # Creative
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=CREATIVE&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "bteam" or servertosearch == "BTeam" or servertosearch == "B-Team" or servertosearch == "Bteam"): # B-Team
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=BTEAM&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "lostislands" or servertosearch == "lost" or servertosearch == "Lost" or servertosearch == "LostIslands"): # Lost Islands
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=LOSTIS&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "Stoneblock2" or servertosearch == "Stoneblock" or servertosearch == "SB2" or servertosearch == "sb2" or servertosearch == "1710" or servertosearch == "1710pack" or servertosearch == "1.7.10" or servertosearch == "1710Pack"): # 1710Pack
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=1710pack&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "pixclassic" or servertosearch == "oldpix" or servertosearch == "PixClassic" or servertosearch == "pixelmonclassic" or servertosearch == "PixelmonClassic"): # Pixelmon Classic
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=PIXELMON&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "pixelmon" or servertosearch == "newpix" or servertosearch == "pix" or servertosearch == "Pixelmon" or servertosearch == "Pix"): # New Pixelmon
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=PIXSPONGE&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "factions" or servertosearch == "facs" or servertosearch == "Factions" or servertosearch == "faction" or servertosearch == "townywithraiding"): # Factions
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=FACTIONS&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "breadandbutter" or servertosearch == "BreadAndButter" or servertosearch == "BreadButter" or servertosearch == "breadbutter" or servertosearch == "BB" or servertosearch == "bb" or servertosearch == "Bread&Butter" or servertosearch == "bread&butter" or servertosearch == "bread" or servertosearch == "Bread"): # Bread & Butter
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=BB&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "tekkit" or servertosearch == "Tekkit"): # Tekkit
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=TEKKIT&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "TekkitLegends" or servertosearch == "tekkitlegends" or servertosearch == "TekkitLegend" or servertosearch == "tekkitlegends" or servertosearch == "Tekkitlegends"): # Tekkit Legends
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=TEKKITLEGENDS&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "prison" or servertosearch == "Prison"): # Prison
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=PRISON&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "wildwest" or servertosearch == "WildWest" or servertosearch == "ww" or servertosearch == "WW"): # Wild West
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=WILDWEST&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "mineqwest" or servertosearch == "MineQwest" or servertosearch == "Mineqwest" or servertosearch == "minequest" or servertosearch == "MineQuest"  or servertosearch == "Minequest" or servertosearch == "qwest" or servertosearch == "Qwest" or servertosearch == "quest" or servertosearch == "Quest"): # MineQwest
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=QWEST&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "parkour" or servertosearch == "Parkour"): # Parkour
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=PARKOUR&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "hungergames" or servertosearch == "HungerGames" or servertosearch == "Hungergames" or servertosearch == "hg" or servertosearch == "HG"): # Hunger Games
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=HG&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "acdc" or servertosearch == "ACDC" or servertosearch == "AutomatedChoas"): # Automated Choas
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=ACDC&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")

        elif(servertosearch == "MCE" or servertosearch == "MCEternal" or servertosearch == "Eternal"): # Automated Choas
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=SFTM&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")
            
        elif(servertosearch == "SkyBlock" or servertosearch == "skyblock" or servertosearch == "Skyblock" or servertosearch == "Sky"): # SkyBlock
            getTime = time.strftime("%Y-%m-%d:%H:%M:%S+0000", gmtime())
            req = urllib3.PoolManager().request("GET","http://www.superfuntime.org/api/mc/pstats2/pstats.php?command=website&&timestamp="+getTime+"&username="+usertosearch+"&info0=info&info1="+usertosearch+"&info2=SKYBLOCK&")
            the_page = req.data
            await ctx.send("```"+re.sub(r"§[A-z0-9]","",the_page.decode("utf-8"))+"```")


#def does_folder_exist():
    #if not os.path.exists("data/sftplayerstats"):
        #print("Creating data/sftplayerstats folder...")
        #os.makedirs("data/sftplayerstats")


#def does_file_exist():
    #file = "data/sftplayerstats/defaultservers.json"
    #if not dataIO.is_valid_json(file):
        #print("Creating empty defaultservers.json...")
        #dataIO.save_json(file, {}) 
