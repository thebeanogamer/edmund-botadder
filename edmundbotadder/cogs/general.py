from discord.ext.commands import Bot, Cog

class General(Cog):
	"""
	Webhook functionality
	"""

	def __init__(self, bot: Bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
		print("Logged in as")
		print(self.bot.user.name)
		print(self.bot.user.id)
		print("------")

def setup(bot):
	bot.add_cog(General(bot))