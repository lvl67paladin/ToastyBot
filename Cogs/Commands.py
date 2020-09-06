import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

import pymongo
from pymongo import MongoClient

#I'm loading all the settings in the cogs, I wonder
#If it's possible to pass all the neccesery info from main?
#Or maybe we can create a file like settings.py and import the same stuff to all cogs?
load_dotenv()

db_cluster = os.getenv('db_cluster')

cluster = MongoClient(db_cluster)
db = cluster["bot_user_data"]
collection = db["bot_user"]
# ^ I don't know what we need for score command
#So, i'm re-dowing everything in main.py

class Com(commands.Cog):

    #initialization
    def __init__(self, bot):
        self.bot = bot

    #The test command
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Yo!")

    # Score command
    @commands.command()
    async def score(self, ctx):
        score=collection.find_one({"_id": ctx.author.id})
        await ctx.send(score["score"])

def setup(bot):
    bot.add_cog(Com(bot))
