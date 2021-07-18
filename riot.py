from riotwatcher import LolWatcher
from sources import API_KEY 
import math
watcher = LolWatcher(API_KEY.key)

def printStats(summonerName):
    
    summoner = watcher.summoner.by_name('euw1', summonerName)
    stats = watcher.league.by_summoner('euw1', summoner['id'])

    try:
        print(summonerName + "\nSolo/Due:" + str(flex_solo(stats, 0)) + "\nFlex 5V5:" + str(flex_solo(stats, 1)))
    except:
        print(summonerName + "\nNo stats")


def flex_solo(stats, pos):
    
    tier = stats[pos]['tier']
    rank = stats[pos]['rank']
    lp = stats[pos]['leaguePoints']
    wins = stats[pos]['wins']
    losses = stats[pos]['losses']
    winrate = wins / (wins + losses)
    return tier, rank, str(lp) + "LP", "winrate :", str(int(math.ceil(winrate * 100))) + "%"

printStats("Name")