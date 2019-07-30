"""Main script to define bot methods, and start the bot."""

from discord.ext.commands import Bot, when_mentioned_or


bot = Bot(command_prefix=when_mentioned_or(":"))


# Load cogs
bot.load_extension("edmundbotadder.cogs.general")
bot.load_extension("edmundbotadder.cogs.commands")
bot.load_extension("edmundbotadder.cogs.webhook")
