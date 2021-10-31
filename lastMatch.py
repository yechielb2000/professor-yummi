from riotwatcher import LolWatcher
from RIOT_API_KEY import key
watcher = LolWatcher(key)
from current_server import SERVER

def getLastMatch(summonerName):
    champ_dict = {}

    latest = watcher.data_dragon.versions_for_region(SERVER)['n']['champion']
    static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')

    summoner = watcher.summoner.by_name(SERVER, summonerName)
    my_matches = watcher.match.matchlist_by_account(SERVER, summoner['accountId'])
    
    last_match = my_matches['matches'][0]
    match_detail = watcher.match.by_id(SERVER, last_match['gameId'])

    participants = []
    for row in match_detail['participants']:
        participants_row = {}
        participants_row['champion'] = row['championId']
        participants_row['win'] = row['stats']['win']
        participants_row['kills'] = row['stats']['kills']
        participants_row['deaths'] = row['stats']['deaths']
        participants_row['assists'] = row['stats']['assists']
        participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
        participants_row['goldEarned'] = row['stats']['goldEarned']
        participants_row['champLevel'] = row['stats']['champLevel']
        participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
        participants.append(participants_row)

    for key in static_champ_list['data']:
        row = static_champ_list['data'][key]
        champ_dict[row['key']] = row['id']   

    # gives me the list of the champions and their on last game
    # for row in participants:
    #     print(str(row['champion']) + ' ' + champ_dict[str(row['champion'])])

    finalTuple = ()
    for participant in participants:
        participantTuple = (champ_dict[str(participant['champion'])], participant['win'], participant['kills'], participant['deaths'], participant['assists'], participant['totalMinionsKilled']) #, participant['totalDamageDealt'], participant['goldEarned'], participant['champLevel']
        finalTuple += (participantTuple,)

    return finalTuple
      
