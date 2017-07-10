import discord
import random
from discord.ext import commands

# Initialize bot with '!' prefix
botTextured = commands.Bot(command_prefix='!')

# games list
games = ['dota 2', 'Battlefield 1', 'minecraft']

@botTextured.event
async def on_ready():
    print("******************")
    print("Starting up bot...")
    print("Username: {}".format(botTextured.user.name))
    print("ID: {}".format(botTextured.user.id))
    print("******************")

@botTextured.command()
async def flip():
    """ choose either heads or tails"""
    num = random.randint(1,10)
    await botTextured.say("flipping coin...")
    if num > 5 and num <= 10:
        await botTextured.say("heads!")
    elif num >= 1 and num <= 5:
        await botTextured.say("tails!")

@botTextured.command()
async def game():
    """ choose a random game in predefined list of games"""
    game = random.choice(games)
    await botTextured.say("{} was chosen!".format(game))

@botTextured.command()
async def feels():
    """ meme a little by sending an emote specific to channel """
    await botTextured.say("<:magiFeels:315987100011069440>")

@botTextured.command()
async def commands():
    """ say list of commands available to the user """
    await botTextured.say("available commands")
    await botTextured.say("!flip !game !feels")

# run bot with token acquired from Discord
botTextured.run("TOKEN_HERE")
