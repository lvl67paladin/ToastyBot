import discord
from discord.ext import commands


#Using this prefix for testing purposes, can be changed later to anything we decide
bot = commands.Bot(coommand_prefix='?')

@bot.event()
async def on_ready():
    print('Bot is ready.')


#I think that other people shouldn't see the bot.run token, so I'll leave it blank
#in the github and add it when we need it
bot.run('')
