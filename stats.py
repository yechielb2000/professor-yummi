from riotwatcher import LolWatcher
from secrets import RIOT_API_KEY 
watcher = LolWatcher(RIOT_API_KEY.key)
import math

def printStats(summonerName):
    
    summoner = watcher.summoner.by_name('euw1', summonerName)
    stats = watcher.league.by_summoner('euw1', summoner['id'])

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






 

   