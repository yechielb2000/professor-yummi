import discord
import json
import commands.champions as champions
from discord.ext import commands
from keep_alive import keep_alive

APP_DATA = json.loads(open("app_data.json").read())
API_KEY = APP_DATA["riot_api_key"]
DISCORD_TOKEN = APP_DATA["discord_token"]
client = commands.Bot(command_prefix="!")


# TODO: refactor this page
@client.event
async def on_ready():
    print(f"Bot is ready as {client.user}")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(error)


@client.command(
    aliases=["changeServer", "change", "change-server"],
    help="Change server (eune1, euw1, etc..).",
)
@client.command(help="This command will clear messages")
async def clear(ctx, amount: int = 1):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=["rank"], help="This command will give you summoner stats")
async def stats(ctx, *, summonerName):
    await ctx.send(summonerStats.printStats(summonerName))


@client.command(help="This command will give you mastry levels of champions")
async def mastery(ctx, summonerName, championName):
    await ctx.send(champions.get_mastery(summonerName, championName))


@client.command(help="This command will give you all champions in alphabetical order")
async def allChampions(ctx):
    await ctx.send(champions.getAllChampions())


@client.command(help="This command will return the information of the entered champion")
async def champion(ctx, championName):
    await ctx.send(champions.get_champion_info(championName))


@client.command(help="This command will give you a full stats of the last game")
async def lastMatch(ctx: commands.Context, *, summonerName):
    DATASET = getLastMatch(summonerName)
    highlight = [
        "champion      win      Kills      Deaths      assists      cs"
    ]  #  total-damage  gold-earned  champion-level
    description = "```" + "\n".join(highlight) + "```"
    i = 0
    for data in DATASET:
        highlight.append(
            ((" " * 6) + (" " * len(highlight[0].split(" " * 6)[0]))).join(
                [str(item).center(0) for item in data]
            )
        )
        # highlight.append((str(highlight[0].split(" " * 6)[i]) + ' - ').join(data))
        # print(data)
        i += 1

    description = "```" + "\n".join(highlight) + "```"
    await ctx.send(
        embed=discord.Embed(title="Last Match Stats", description=description)
    )
    print(highlight)


keep_alive()
client.run(DISCORD_TOKEN)
