import discord
import stat
import champions_stats
import lastMatch
from discord import message
from discord.ext import commands
from sources import DISCORD_TOKEN


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(help='this command will clear messages')
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['rank'], help='this command will give you summoner stats')  
async def stats(ctx, *, summonerName):
    await ctx.send(stat.printStats(summonerName))

# Currently not finished
# @client.command(help="this command will give you mastry champions of champion")
# async def mastry(ctx, *, summonerName, championName):
#     await ctx.send(stat.getMastry(summonerName, championName))    

@client.command(help="this command will give you all champions with their id")
async def allChampions(ctx):
    await ctx.send(champions_stats.getAllChampions())

@client.command()
async def lastMatch(ctx: commands.Context, *, summonerName):

    DATASET = lastMatch.getLastMatch(summonerName)

    highlight = ['name     win     Kills     Deaths     assists     cs     total-damage     gold-earned     champion-level']
    
    for data in DATASET:
        highlight.append('   '.join([str(item).center(5, ' ') for item in data]))
   
    description = '```'+'\n'.join(highlight) + '```'

    embed = discord.Embed(title = 'Last Match Stats', description = description)
    await ctx.send(embed = embed)    

client.run(DISCORD_TOKEN.token)   


