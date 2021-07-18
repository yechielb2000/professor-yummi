import discord
from discord import message
from discord.ext import commands
from sources import DISCORD_TOKEN
import riot

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

# this command clear messages (the user can choose how many messages to delete the default is 1)
@client.command()
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit=amount)

# this command let the user know what is the rank stats of a player in euw1 server by typing .stats 'name of summoner'
@client.command(aliases=['rank'])  
async def stats(ctx, *,summonerName):
    await ctx.send(riot.printStats(summonerName))

client.run(DISCORD_TOKEN.token)   
