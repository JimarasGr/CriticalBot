import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
	print(bot.user.name)
	print('is online. ID:')
	print(bot.user.id)
	
@bot.command()
async def hi():
	await bot.say('Hi, I am Critical Bot. Type ?help for a list of commands.')
	
bot.run('NTU4NjQ1MTA2NDIxMzk5NTUy.D3Z_6w.ElI0uWnCQSHyH9Sop1zAI-yt3xU')
