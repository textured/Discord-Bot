import discord
import random
from discord.ext import commands

# Initialize bot with '!' prefix
botTextured = commands.Bot(command_prefix='!')

dotaAPI = dota2api.Initialise("STEAM_WEBAPI_KEY")


"""
Associate dota2 ID's of players with key of discord ID
e.g 'sample#0123': 11111111
"""
usersDotaID = {
"sample#0123": 11111111
}


# games list
games = ["insert example games here"]

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

# Dota 2 related commands

@botRaymond.command(pass_context=True)
async def recentgame(ctx):
    """
    Retrives link to latest dota game dependant on caller via dotabuff

    """
    url = 'https://www.dotabuff.com/matches/'
    user_id = str(ctx.message.author)
    dota_id = usersDotaID[user_id]
    hist = dotaAPI.get_match_history(account_id=dota_id)
    matchid = str(hist['matches'][0]['match_id'])
    await botRaymond.say(content="{}".format(url + matchid))

@botRaymond.command(pass_context=True)
async def dotabuff(ctx, arg = None):
    """
    Retrive dotabuff account (Optional argument to perform search)
    e.g !dotabuff Dendi performs a search for users named Dendi

    """
    if arg == None:
        url = 'https://www.dotabuff.com/players/'
        user_id = str(ctx.message.author)
        player_id = str(usersDotaID[user_id])
        await botRaymond.say(content="{}".format(url + player_id))
    elif arg != None:
        url = 'https://www.dotabuff.com/search?utf8=%E2%9C%93&q={}&commit=Search'.format(arg)
        await botRaymond.say(content="{}".format(url))

# run bot with token acquired from Discord
botTextured.run("TOKEN_HERE")
