import discord
from discord.ext import commands


#Using this prefix for testing purposes, can be changed later to anything we decide
bot = commands.Bot(command_prefix='?')



@bot.command()
async def Test(ctx):
    await ctx.send('Yo!')

#I think that other people shouldn't see the bot.run token, so I'll leave it blank
#in the github and add it when we need it
try:
    bot.run('token')
except Exception as e:
    print(f"problem logging in:{e}")
