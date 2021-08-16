from riotwatcher import LolWatcher
from sources import RIOT_API_KEY 
watcher = LolWatcher(RIOT_API_KEY.key)

def getMastry(summonerName, mastryChampion):
    # not complitted
    summoner = watcher.summoner.by_name('euw1', summonerName)
    mastry = watcher.champion_mastery.by_summoner('euw1', summoner['id'])
   
    championMastry = watcher.champion_mastery.by_summoner_by_champion(summoner['id'], champion_id=3)
    print('result')
    print(championMastry)
    # print(mastry)

def getAllChampions():
   
    latest = watcher.data_dragon.versions_for_region('euw1')['n']['champion']
    static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')
    
    champs = ''
    tempKey = 'A'
    for key in static_champ_list['data']:
        if tempKey[0] == key[0]:
             champs += key + ' ' 
        else : 
            champs += '\n'+key[0]+':\n' + key + ' '

        tempKey = key    
      
    return '\nVersion : ' + static_champ_list['version'] + '\nA:\n' + champs
