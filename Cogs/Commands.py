import discord
from discord.ext import commands
import os
from dotenv import load_dotenv



class Com(commands.Cog):

    #initialization
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Command Cog is here too")


    #The test command
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Yo!")



def setup(bot):
    bot.add_cog(Com(bot))
