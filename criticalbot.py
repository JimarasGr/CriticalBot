import discord
from discord.ext import commands
import asyncio
import json

TOKEN = 'NTU4NjQ1MTA2NDIxMzk5NTUy.D3Z_6w.ElI0uWnCQSHyH9Sop1zAI-yt3xU'

with open('prefix.json') as f:
	prefix = f.read()

client = commands.Bot(command_prefix=prefix)

client.remove_command('help')

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='Critical Ops | ?help'))
	print(client.user.name + ' is logged in discord.')
	print('ID: ' + client.user.id)

#Settings-Info
@client.command()
async def prefix():
	await client.say('My prefix is \"?" and you cannot set your own prefix at the moment.')

@client.command()
async def commands():
	await client.say('For a list of commands type \"?help".')
	
@client.command(pass_context=True)
async def help(ctx):
	
	embed = discord.Embed(
		title = '-----------------------',
		colour = discord.Colour.blue()
	)
	
	embed.set_author(name='Command List', icon_url='https://images.app.goo.gl/paxz6aJrxo17QjR3A')
	
	embed.add_field(name='Settings and Info', value='--------------------', inline=False)
	
	embed.add_field(name='?prefix', value='shows you its prefix, well it is obvious but ok!')
	
	embed.add_field(name='Fun Commands', value='--------------------', inline=False)
	
	embed.add_field(name='?hi', value='says hi', inline=False)
	
	embed.add_field(name='?ping', value='says pong', inline=False)

	embed.add_field(name='?creator', value='who is the master?', inline=False)
	
	embed.add_field(name='C-OPS Rank', value='--------------------', inline=False)
	
	embed.add_field(name='?unranked', value='Sets your C-OPS rank to Unranked', inline=False)
	
	embed.add_field(name='?bronze', value='Sets your C-OPS rank to Bronze', inline=False)
	
	embed.add_field(name='?silver', value='Sets your C-OPS rank to Silver', inline=False)
	
	embed.add_field(name='?gold', value='Sets your C-OPS rank to Gold', inline=False)
	
	embed.add_field(name='?platinum', value='Sets your C-OPS rank to Platinum', inline=False)
	
	embed.add_field(name='?diamond', value='Sets your C-OPS rank to Diamond', inline=False)
	
	embed.add_field(name='?master', value='Sets your C-OPS rank to Master', inline=False)
	
	embed.add_field(name='?specops', value='Sets your C-OPS rank to Spec Ops', inline=False)

	await client.say(embed=embed)

#Fun Commands
@client.command()
async def hi():
	await client.say('Hi, I am Critical Bot. Type \"?help" for a list of commands.')

@client.command()
async def ping():
	await client.say('pong!')

@client.command()
async def creator():
	await client.say('JimarasGr made me and he is my master!')

#C-OPS Rank
@client.command(pass_context=True)
async def unranked(ctx):
	author = ctx.message.author
	
	role = discord.utils.get(author.server.roles, name='Unranked')
	await client.add_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Bronze')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Silver')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Gold')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Platinum')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Diamond')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Master')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Spec Ops')
	await client.remove_roles(author, role)
	
	await client.say('Your C-OPS rank has been set to Unranked')
	
@client.command(pass_context=True)
async def bronze(ctx):
	author = ctx.message.author
	
	role = discord.utils.get(author.server.roles, name='Bronze')
	await client.add_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Unranked')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Silver')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Gold')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Platinum')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Diamond')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Master')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Spec Ops')
	await client.remove_roles(author, role)
	
	await client.say('Your C-OPS rank has been set to Bronze')
	
@client.command(pass_context=True)
async def silver(ctx):
	author = ctx.message.author
	
	role = discord.utils.get(author.server.roles, name='Silver')
	await client.add_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Bronze')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Unranked')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Gold')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Platinum')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Diamond')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Master')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Spec Ops')
	await client.remove_roles(author, role)
	
	await client.say('Your C-OPS rank has been set to Silver')
	
@client.command(pass_context=True)
async def gold(ctx):
	author = ctx.message.author
	
	role = discord.utils.get(author.server.roles, name='Gold')
	await client.add_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Bronze')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Silver')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Unranked')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Platinum')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Diamond')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Master')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Spec Ops')
	await client.remove_roles(author, role)
	
	await client.say('Your C-OPS rank has been set to Gold')
	
@client.command(pass_context=True)
async def platinum(ctx):
	author = ctx.message.author
	
	role = discord.utils.get(author.server.roles, name='Platinum')
	await client.add_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Bronze')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Silver')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Gold')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Unranked')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Diamond')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Master')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Spec Ops')
	await client.remove_roles(author, role)
	
	await client.say('Your C-OPS rank has been set to Platinum')
	
@client.command(pass_context=True)
async def diamond(ctx):
	author = ctx.message.author
	
	role = discord.utils.get(author.server.roles, name='Diamond')
	await client.add_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Bronze')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Silver')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Gold')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Platinum')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Unranked')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Master')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Spec Ops')
	await client.remove_roles(author, role)
	
	await client.say('Your C-OPS rank has been set to Diamond')
	
@client.command(pass_context=True)
async def master(ctx):
	author = ctx.message.author
	
	role = discord.utils.get(author.server.roles, name='Master')
	await client.add_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Bronze')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Silver')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Gold')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Platinum')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Diamond')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Unranked')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Spec Ops')
	await client.remove_roles(author, role)
	
	await client.say('Your C-OPS rank has been set to Master')
	
@client.command(pass_context=True)
async def specops(ctx):
	author = ctx.message.author
	
	role = discord.utils.get(author.server.roles, name='Spec Ops')
	await client.add_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Bronze')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Silver')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Gold')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Platinum')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Diamond')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Master')
	await client.remove_roles(author, role)
	
	role = discord.utils.get(author.server.roles, name='Unranked')
	await client.remove_roles(author, role)
	
	await client.say('Your C-OPS rank has been set to Spec Ops')

client.run(TOKEN)
