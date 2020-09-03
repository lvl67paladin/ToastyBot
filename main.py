import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

import pymongo
from pymongo import MongoClient

load_dotenv()
token=os.getenv('token')

db_cluster=os.getenv('db_cluster')
#Using this prefix for testing purposes, can be changed later to anything we decide
bot = commands.Bot(command_prefix='?')

#MongoDB cluster
cluster = MongoClient(db_cluster)
db = cluster["bot_user_data"]
collection = db["bot_user"]

@bot.event
async def on_ready(ctx):
    print("logging in")
    await  ctx.send("logged in")

@bot.command()
async def test(ctx):
    await ctx.send('Yo!')





@bot.event
async def on_message(ctx):
    print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")
    myquery = {"_id": ctx.author.id}
    #first check if the message is from bot itelf
    if ctx.author==bot.user:
        await bot.process_commands(ctx)
        
    if "money" in str(ctx.content.lower()):
        await ctx.channel.send("here! take some coins you pityful creature")
    
    if (collection.count_documents(myquery) == 0):
        if "crispy" in str(ctx.content.lower()):
            post = {"_id": ctx.author.id, "score": 1}
            collection.insert_one(post)
            await ctx.channel.send('accepted!')
    else:
        if "crispy" in str(ctx.content.lower()):
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            for result in user:
                score = result["score"]
            score = score + 1
            collection.update_one({"_id":ctx.author.id}, {"$set":{"score":score}})
            await ctx.channel.send('accepted!')
    #very important..we need to call this otherwise commands won't work
    await bot.process_commands(ctx)
   
@bot.command()
async def score(ctx):
    score=collection.find_one({"_id": ctx.author.id})
    await ctx.send(score["score"])


#I think that other people shouldn't see the bot.run token, so I'll leave it blank
#in the github and add it when we need it
try:
    bot.run(token)
except Exception as e:
    print(f"problem logging in:{e}")
