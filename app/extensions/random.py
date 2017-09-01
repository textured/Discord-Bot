import discord
import dota2api
import random
import urllib.request
import urllib.parse
import json
import urllib
import time

from bs4 import BeautifulSoup
from discord.ext import commands

class Random():
    def __init__(self, bot):
        self.bot = bot
        # games list
        self.games = ["insert example games here"]

    @commands.command()
    async def flip(self):
        """ choose either heads or tails"""
        num = random.randint(1,10)
        await self.bot.say("flipping coin...")
        if num > 5 and num <= 10:
            await self.bot.say("heads!")
        elif num >= 1 and num <= 5:
            await self.bot.say("tails!")

    @commands.command()
    async def game(self):
        """ choose a random game in predefined list of games"""
        game = random.choice(games)
        await self.bot.say("{} was chosen!".format(game))


    @commands.command()
    async def feels(self):
        """ meme a little by sending an emote specific to channel """
        await self.bot.say("<:magiFeels:315987100011069440>")

def setup(bot):
    bot.add_cog(Random(bot))
