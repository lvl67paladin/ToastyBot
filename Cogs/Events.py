import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

import pymongo
from pymongo import MongoClient

load_dotenv()

db_cluster = os.getenv('db_cluster')

cluster = MongoClient(db_cluster)
db = cluster["bot_user_data"]
collection = db["bot_user"]
# Same reason as I mentioned in Commans.py

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Event Cog is ready for some action")

    #Dd's messy command. It also doesn't work
    @commands.Cog.listener()
    async def on_message(self, ctx):
        #print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")
        myquery = {"_id": ctx.author.id}
        #first check if the message is from bot itelf
        if ctx.author==self.bot.user:
            await self.bot.process_commands(ctx)

        if "stream" in str(ctx.content.lower()):
            await ctx.channel.send("simp!")

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
        await self.bot.process_commands(ctx)


def setup(bot):
    bot.add_cog(Events(bot))
