from discord.ext.commands import Bot, Cog

class Webhook(Cog):
	"""
	Webhook functionality
	"""

	def __init__(self, bot: Bot):
		self.bot = bot

def setup(bot):
	bot.add_cog(Webhook(bot))