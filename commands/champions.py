from base_lol_command import BaseLolCommand
from typing import Dict, List, Any


class Champion:
    DATA = "data"
    INFO = "info"
    STATS = "stats"
    KEY = "key"
    KEYS = "keys"


class Champions(BaseLolCommand):
    def __init__(self, api_key: str, server: str = ...) -> None:
        super().__init__(api_key, server)
        self.champions_data = self.champions_list[Champion.DATA]
        self.champions_keys = self.champions_list[Champion.KEYS]

    def get_champions_list(self) -> List[str]:
        return "\n".join(name for name in self.champions_keys.values())

    def get_champion_info(self, champion_name: str) -> Dict[str, Any]:
        return self.champions_data[champion_name.capitalize()][Champion.INFO]

    def get_champion_stats(self, champion_name: str) -> Dict[str, Any]:
        return self.champions_data[champion_name.capitalize()][Champion.STATS]
