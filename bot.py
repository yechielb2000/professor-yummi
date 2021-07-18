import discord
from discord.ext import commands
from sources import DISCORD_TOKEN
import riot

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()  
async def stats(contex, *,summonerName):
    await contex.send(riot.printStats(summonerName))

client.run(DISCORD_TOKEN.token)   
