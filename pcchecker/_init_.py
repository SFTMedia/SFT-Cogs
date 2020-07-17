from .pcchecker import PCChecker

def setup(bot):
	bot.add_cog(PCChecker(bot))