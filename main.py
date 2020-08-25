import discord
from discord.ext import commands


#Using this prefix for testing purposes, can be changed later to anything we decide
bot = commands.Bot(command_prefix='?')

@bot.event()
async def on_ready(ctx):
    print('Bot is ready.')
    #This bellow command? Yes, it doesn't work :(
    await ctx.send("Hey you're finally awake... NO! I am finally awake")

@bot.command()
async def Test(ctx):
    await ctx.send('Yo!')

#I think that other people shouldn't see the bot.run token, so I'll leave it blank
#in the github and add it when we need it
bot.run('')
