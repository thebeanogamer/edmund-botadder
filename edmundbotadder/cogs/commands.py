from discord.ext.commands import Bot, Cog

class Commands(Cog):
	"""
	Command functionality
	"""

	def __init__(self, bot: Bot):
		self.bot = bot

def setup(bot):
	bot.add_cog(Commands(bot))