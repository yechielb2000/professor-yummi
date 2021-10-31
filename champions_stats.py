from RIOT_API_KEY import key
from riotwatcher import LolWatcher
watcher = LolWatcher(key)
from current_server import SERVER

latest = watcher.data_dragon.versions_for_region(SERVER)['n']['champion']
champs_list = watcher.data_dragon.champions(latest, False, 'en_US')

def getMastry(summonerName, search):
   
    champ_key = None
    for champion in champs_list['data']:
        if champion.lower() == search.lower():
            champ_key = champs_list['data'][f'{champion}']['key']

    summoner = watcher.summoner.by_name(SERVER, summonerName)
    championMastry = watcher.champion_mastery.by_summoner_by_champion(SERVER, summoner['id'], champion_id=champ_key)
    print("Champion Level : " + str(championMastry['championLevel']) + "\nChampion Points : " + str(championMastry['championPoints']) + "\nChampion Tokens : " + str(championMastry['tokensEarned']) + "\nChest Granted : " + str(championMastry['chestGranted']))

def getAllChampions():

    champs = ''
    tempKey = 'A'
    for key in champs_list['data']:
        if tempKey[0] == key[0]:
             champs += key + ' ' 
        else : 
            champs += '\n' + key[0]+': ' + key + ' '

        tempKey = key    
      
    return '\nVersion : ' + champs_list['version'] + '\nA: ' + champs

def getChampionStats(search):

    champ_stats = ''
    for champion in champs_list['data']:
        if champion.lower() == search.lower():
            data = champs_list['data'][f'{champion}']

            champ_stats += "Attack : "  + str(data['info']['attack']) + "\nDefense : "  + str(data['info']['defense']) + "\nDifficulty : "  + str(data['info']['difficulty']) + "\nMagic : "  + str(data['info']['magic'])
            champ_stats += "\n\nChampion Class : " 

            for tag in data['tags']:
                champ_stats += f"{tag} "
            
            champ_stats += "\nPartype : " + data['partype']

            champ_stats += "\n\nStats\n"

            for status in data['stats']:
                champ_stats += f"{status} : {data['stats'][f'{status}']} \n"

            return champ_stats
    