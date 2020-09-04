#!/usr/bin/python
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


# Trying to implement cogs idk.
#A command to load a cog
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'Cogs.{extension}')

#A command to unload a cog
#Tho, idk if we need load and unload process_commands
#So, random peeps won't be able to unload the commands
#It might be usefull for testing stuff tho
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')

#Another usefull testing command for relading cogs
@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')
    bot.load_extension(f'Cogs.{extension}')

#Loading all cogs
for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')


try:
    bot.run(token)
except Exception as e:
    print(f"problem logging in:{e}")
