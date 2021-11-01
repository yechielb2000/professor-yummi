import discord
import stats as summonerStats
import champions_stats
from lastMatch import getLastMatch
from discord.ext.commands import CommandNotFound
from discord.ext import commands
import current_server
import DISCORD_TOKEN
from keep_alive import keep_alive

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print(f'Bot is ready as {client.user}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(error)    

@client.command(aliases=["changeServer", "change", "changeserver"], help='This command will change current server')
async def server(ctx, serverName):
    current_server.SERVER = serverName + str(1)
    await ctx.send("current server is : ", current_server.SERVER)

@client.command(help='This command will clear messages')
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['rank'], help='This command will give you summoner stats')  
async def stats(ctx, *, summonerName):
    await ctx.send(summonerStats.printStats(summonerName))

@client.command(help="This command will give you mastry levels of champions")
async def mastery(ctx, summonerName, championName):
    await ctx.send(champions_stats.getMastry(summonerName, championName))    

@client.command(help="This command will give you all champions in alphabetical order")
async def allChampions(ctx):
    await ctx.send(champions_stats.getAllChampions())

@client.command(help="This command will return the information of the entered champion")
async def champion(ctx, championName):
    await ctx.send(champions_stats.getChampionInfo(championName))

@client.command(help="This command will give you a full stats of the last game")
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
    
keep_alive()
client.run(DISCORD_TOKEN.token)   


