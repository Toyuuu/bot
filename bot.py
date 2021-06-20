import os

os.system("pip install discord")
os.system("cls")


os.system("title " + "Made by Toyu#9922")


import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=['!'], self_bot=False)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def hello(ctx):
	await ctx.send("hello")
	
bot.run("")