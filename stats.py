from RIOT_API_KEY import key
from riotwatcher import LolWatcher
watcher = LolWatcher(key)
from current_server import SERVER
import math

def printStats(summonerName):
    
    summoner = watcher.summoner.by_name(SERVER, summonerName)
    stats = watcher.league.by_summoner(SERVER, summoner['id'])

    try:
        return 'Level : ' + str(summoner['summonerLevel']) + "\n" + 'Flex 5v5 : ' + flex_solo(stats, 0)[0] + " " + flex_solo(stats, 0)[1] + " " + flex_solo(stats, 0)[2] + " " + flex_solo(stats, 0)[3] + "\n" + 'Solo Due : ' +  flex_solo(stats, 1)[0] + " " + flex_solo(stats, 1)[1] + " " + flex_solo(stats, 1)[2] + " " + flex_solo(stats, 1)[3]
    except:
        return summonerName + "\nNo stats"

def flex_solo(stats, pos):
    
    tier = stats[pos]['tier']
    rank = stats[pos]['rank']
    lp = stats[pos]['leaguePoints']
    wins = stats[pos]['wins']
    losses = stats[pos]['losses']
    winrate = wins / (wins + losses)

    result =  [tier, rank, str(lp) + "LP", "with " + str(int(math.ceil(winrate * 100))) + "% winrate"]
    return result






 

   