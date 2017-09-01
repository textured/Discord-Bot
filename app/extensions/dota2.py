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

class Dota2():
    def __init__(self, bot):
        self.bot = bot
        self.dotaAPI = dota2api.Initialise("STEAM_WEBAPI_KEY")

        # Associate dota2 ID's of players with key of discord ID e.g 'sample#0123': 11111111
        self.usersDotaID = {
        "sample#0123": 11111111
        }


    @commands.command(pass_context=True)
    async def recentgame(self, ctx, arg=None):
        """
        Retrives link to latest dota game dependant on caller via dotabuff
        optional parameter [stats] which displays quick info on player performance

        """
        try:
            url = 'https://www.dotabuff.com/matches/'
            user_id = str(ctx.message.author)
            dota_id = self.usersDotaID[user_id]
            hist = self.dotaAPI.get_match_history(account_id=dota_id)
            matchid = str(hist['matches'][0]['match_id'])

            if arg == None:
                await self.bot.say(content="{}".format(url + matchid))

            if arg == 'stats':
                match_info = self.dotaAPI.get_match_details(match_id = int(matchid))
                for player in match_info['players']:
                    if player['account_id'] == dota_id:
                        await self.bot.say(content='```''
                                           'Hero:        {}\n'
                                           'K/D/A:       {}/{}/{}\n'
                                           'Last hits:   {}\n'
                                           'GPM:         {}\n'
                                           'XPM:         {}```'.format(
                                           player['hero_name'], player['kills'], player['deaths'],
                                           player['assists'], player['last_hits'], player['gold_per_min'],
                                           player['xp_per_min']))
        except APITimeoutError:
            await self.bot.say(content="Valve API currently down! Try again later.")

    @commands.command(pass_context=True)
    async def dotabuff(self, ctx, arg = None):
        """
        Retrive dotabuff account (Optional argument to perform search)
        e.g !dotabuff Dendi performs a search for users named Dendi

        """
        if arg == None:
            url = 'https://www.dotabuff.com/players/'
            user_id = str(ctx.message.author)
            player_id = str(self.usersDotaID[user_id])
            await self.bot.say(content="{}".format(url + player_id))
        elif arg != None:
            url = 'https://www.dotabuff.com/search?utf8=%E2%9C%93&q={}&commit=Search'.format(arg)
            await self.bot.say(content="{}".format(url))

    @commands.command(pass_context=True)
    async def mymmr(ctx):
        """
        Displays information about dota profile such as solo, party and estimated matchmaking rating (mmr)
        """
        base_url = "https://api.opendota.com/api/players/"
        discord_id = str(ctx.message.author)
        search_url = base_url + str(self.usersDotaID[discord_id])
        with urllib.request.urlopen(search_url) as url:
            data = json.loads(url.read().decode())

        await self.bot.say(content='```'
                           'steam name:    {}\n'
                           'solo mmr:      {}\n'
                           'party mmr:     {}\n'
                           'estimated mmr: {}\n```'.format(
                           match['profile']['personaname'], match['solo_competitive_rank'],
                           match['competitive_rank'], match['mmr_estimate']['estimate']))

def setup(bot):
    bot.add_cog(Dota2(bot))
