import discord
import stat
import champions_stats
from lastMatch import getLastMatch
from discord import message
from discord.ext.commands import CommandNotFound
from discord.ext import commands
from current_server import SERVER
import DISCORD_TOKEN

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(error)    

@client.command(aliases=["changeServer", "server", "changeserver"], help='this command will change current server')
async def change(ctx, serverName = "euw1"):
    global SERVER
    ctx.send("Your options are : euw1, eun1, na1")
    SERVER = serverName
    await ctx.send("current server is : ", SERVER)

@client.command(help='this command will clear messages')
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['rank'], help='this command will give you summoner stats')  
async def stats(ctx, *, summonerName):
    await ctx.send(stat.printStats(summonerName))

# Currently not finished
# @client.command(help="this command will give you mastry levels of champions")
# async def mastry(ctx, *, summonerName, championName):
#     await ctx.send(stat.getMastry(summonerName, championName))    

@client.command(help="this command will give you all champions with their id")
async def allChampions(ctx):
    await ctx.send(champions_stats.getAllChampions())

@client.command(help="this command will give you a full stats of the last game")
async def lastMatch(ctx: commands.Context, *, summonerName):
    DATASET = getLastMatch(summonerName)

    highlight = ['champion      win      Kills      Deaths      assists      cs'] #  total-damage  gold-earned  champion-level
    description = '```'+'\n'.join(highlight) + '```'
    
    i = 0
    for data in DATASET:
        highlight.append(((" " * 6) + (" " * len(highlight[0].split(" "*6)[0]))).join([str(item).center(0) for item in data]))
        # highlight.append((str(highlight[0].split(" " * 6)[i]) + ' - ').join(data))
        # print(data)
        i += 1

    description = '```'+'\n'.join(highlight) + '```'
    await ctx.send(embed = discord.Embed(title = 'Last Match Stats', description = description))
    print(highlight)
    

client.run(DISCORD_TOKEN.token)   


