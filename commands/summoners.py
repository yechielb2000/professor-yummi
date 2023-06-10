from base_lol_command import BaseLolCommand
from typing import Dict, Any


class Summoners(BaseLolCommand):
    def __init__(self, summoner_name: str, api_key: str, server: str) -> None:
        super().__init__(api_key, server)
        self.summoner_name = summoner_name
        self.summoner = self.watcher.summoner.by_name(self.region, self.summoner_name)

    def get_stats(self) -> Dict[str, Any]:
        return self.watcher.league.by_summoner(self.region, self.summoner["id"])

    def get_last_match(self) -> Dict[str, Any]:
        matches = self.watcher.match.matchlist_by_account(
            self.region, self.summoner["accountId"]
        )
        last_match = matches["matches"][0]
        match_details = self.watcher.match.by_id(self.region, last_match["gameId"])
        return match_details

    def get_champion_mastery(self, champion_name: str) -> Dict[str, Any]:
        champion_key = self.champions_list["data"][champion_name.capitalize()]["key"]
        champion_mastery = self.watcher.champion_mastery.by_summoner_by_champion(
            self.region, self.summoner["id"], champion_id=champion_key
        )
        return champion_mastery
