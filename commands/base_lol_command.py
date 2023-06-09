from riotwatcher import LolWatcher


REGION = "eune1"


class BaseLolCommand:
    def __init__(self, api_key: str, region: str = REGION) -> None:
        self.region = region
        self.watcher = LolWatcher(api_key=api_key)
        self.latest_version = self.watcher.data_dragon.versions_for_region(self.region)[
            "n"
        ]["champion"]
        self.champions_list = self.watcher.data_dragon.champions(
            version=self.latest_version, full=True, locale="en_US"
        )
