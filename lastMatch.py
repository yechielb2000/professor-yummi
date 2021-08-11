from riotwatcher import LolWatcher
from sources import API_KEY 
watcher = LolWatcher(API_KEY.key)

def getLastMatch(summonerName):
    champ_dict = {}

    latest = watcher.data_dragon.versions_for_region('euw1')['n']['champion']
    static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')

    summoner = watcher.summoner.by_name('euw1', summonerName)
    my_matches = watcher.match.matchlist_by_account('euw1', summoner['accountId'])
    
    last_match = my_matches['matches'][0]
    match_detail = watcher.match.by_id('euw1', last_match['gameId'])

    participants = []
    for row in match_detail['participants']:
        participants_row = {}
        participants_row['champion'] = row['championId']
        # participants_row['spell1'] = row['spell1Id']
        # participants_row['spell2'] = row['spell2Id']
        participants_row['win'] = row['stats']['win']
        participants_row['kills'] = row['stats']['kills']
        participants_row['deaths'] = row['stats']['deaths']
        participants_row['assists'] = row['stats']['assists']
        participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
        participants_row['goldEarned'] = row['stats']['goldEarned']
        participants_row['champLevel'] = row['stats']['champLevel']
        participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
        # participants_row['item0'] = row['stats']['item0']
        # participants_row['item1'] = row['stats']['item1']
        participants.append(participants_row)

    for key in static_champ_list['data']:
        row = static_champ_list['data'][key]
        champ_dict[row['key']] = row['id']   

    # gives me the list of the champions and their on last game
    # for row in participants:
    #     print(str(row['champion']) + ' ' + champ_dict[str(row['champion'])])

    finalTuple = ()
    for participant in participants:
        participantTuple = (champ_dict[str(participant['champion'])], participant['win'], participant['kills'], participant['deaths'], participant['assists'], participant['totalMinionsKilled'], participant['totalDamageDealt'], participant['goldEarned'], participant['champLevel'])
        finalTuple += (participantTuple,)

    return finalTuple
      
