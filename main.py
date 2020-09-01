import discord
from discord.ext import commands

import pymongo
from pymongo import MongoClient

#MongoDB cluster
cluster = MongoClient("mongodb+srv://dbusertest:dbuserpass@cluster0.f23tr.mongodb.net/test")

collection = db["bot_user_data"]

@bot.event
async def on_message(ctx): 
  print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")
  if "toasty" or "crispy" or "toasted" in str(ctx.content.lower()):
    score = {"id": ctx.author.id, "count": 1}
    collection.insert_one(score)
    await ctx.send("counted!")



#Using this prefix for testing purposes, can be changed later to anything we decide
bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready(ctx):
    print("logging in")
    await  ctx.send("logged in")

@bot.command()
async def Test(ctx):
    await ctx.send('Yo!')

#I think that other people shouldn't see the bot.run token, so I'll leave it blank
#in the github and add it when we need it
try:
    bot.run('NTA3Nzc3OTQ1NjA4MjU3NTM3.W9vXEA.wGVaypo5CXlbnJuMaiU4clgP0FQ')
except Exception as e:
    print(f"problem logging in:{e}")
