from .sftplayerstats import SFTPlayerStats

def setup(bot):
	bot.add_cog(SFTPlayerStats(bot))