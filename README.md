# Discord-Bot
Discord bot to assist with everyday activities

# Setup 
###### (Recommended for those who know at least basic programming)
First create your bot account to use with your website by following the link belowed while logged into Discord on your web browser:


[Create bot](https://discordapp.com/developers/applications/me)

1. Create a new application
2. Give it a *brand new name*, description and icon!
3. Click on *create Bot user* and confirm your action
4. Find your token under the APP BOT USER and save it for use with the bot
5. Edit the bot.py file in the app folder and place your token in the string on the line **botTexured.run('TOKEN HERE')**
6. Get your steam API key from [here](https://steamcommunity.com/dev/apikey)
7. Place your Steam web api in the line and replace the string dotaAPI = **dota2api.Initialise("STEAM_WEBAPI_KEY")**
8  Edit the dictionaries games and usersDotaID for usage of the dota commands and game command
9. Lastly, run the python file in the app folder through the command *python3 bot.py* 


# Commands
_brackets reflect optional paramters to the command_

##### !dotabuff [search query]
- pulls up dotabuff link to player calling command, or performs a search  
##### !recentgame [stats]
- returns a link to match via dotabuff depending on who called the command or stats of recent game if stats is called in command
##### !mymmr
- brings up information about mmr of person who invoked the command
##### !help
- gives detailed information of list of commands avaliable to users
