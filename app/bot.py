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

# Initialize bot with '!' prefix
botTextured = commands.Bot(command_prefix='!', description='beep boop bot to help with dota')

initial_time = time.time()
extensions = ["extensions.random", "extensions.dota2"]

@botTextured.event
async def on_ready():
    print("******************")
    print("Starting up bot...")
    print("Username: {}".format(botTextured.user.name))
    print("ID: {}".format(botTextured.user.id))
    print("******************")

    for extension in extensions:
        botTextured.load_extension(extension)

@botTextured.command()
async def uptime():
    # not accounting for days yet since it won't be up for that long anyways
    """ Displays how long bot has been up """
    sec = time.time() - initial_time
    mins, seconds = divmod(sec, 60)
    hours, minutes = divmod(mins, 60)
    await botTextured.say(content="BOT Textured has been up for {} hours, {} minutes, {} seconds".format(int(hours), int(minutes), int(seconds)))

# run bot with token acquired from Discord
botTextured.run("TOKEN_HERE")
