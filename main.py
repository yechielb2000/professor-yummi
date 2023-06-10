import json

from keep_alive import keep_alive
from discord.ext.commands import Context, CommandNotFound, Bot
from commands.champions import Champions
from commands.summoners import Summoners


APP_DATA = json.loads(open("app_data.json").read())
API_KEY = APP_DATA["riot_api_key"]
DISCORD_TOKEN = APP_DATA["discord_token"]
SERVER = "eune1"
client = Bot(command_prefix="!")


@client.event
async def on_ready():
    print(f"Bot is ready as {client.user}")


@client.event
async def on_command_error(ctx: Context, error: CommandNotFound):
    if isinstance(error, CommandNotFound):
        await ctx.send(error)


@client.command(
    help="Clear messages, amount=number of messages to delete.\ndefault is 1."
)
async def clear(ctx: Context, amount: int = 1):
    await ctx.channel.purge(limit=amount)


@client.command(help="Get champions list")
async def champions_list(ctx: Context, s: str = SERVER):
    champion = Champions(API_KEY, s)
    await ctx.send(champion.get_champions_list())


@client.command(help="Get info of certain champion")
async def champion(
    ctx: Context, champion_name: str, full_stats: bool = False, s: str = SERVER
):
    champion = Champions(API_KEY, s)
    if full_stats:
        champion_data = dict()
        champion_data['info'] = await champion.get_champion_info(champion_name)
        champion_data['stats'] = await champion.get_champion_stats(champion_name)
        ctx.send(champion_data)
    else:
        await ctx.send(champion.get_champion_info(champion_name))


@client.command(help="Get mastery of specific champion")
async def mastery(
    ctx: Context, summoner_name: str, champion_name: str, s: str = SERVER
):
    summoner = Summoners(summoner_name, API_KEY, s)
    await ctx.send(summoner.get_champion_mastery(champion_name))


@client.command(help="Get full stats of the last game")
async def last_match(ctx: Context, summoner_name: str, s: str = SERVER):
    summoner = Summoners(summoner_name, API_KEY, s)
    await ctx.send(summoner.get_last_match())


@client.command(help="Get summoner stats")
async def summoner(ctx: Context, summoner_name: str, s: str = SERVER):
    summoner = Summoners(summoner_name, API_KEY, s)
    await ctx.send(summoner.get_stats())


if __name__ == "__main__":
    keep_alive()
    client.run(DISCORD_TOKEN)
