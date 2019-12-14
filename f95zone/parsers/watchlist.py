import re


from f95zone.patterns.watchlist import WatchlistPattern
from f95zone.patterns.f95url import F95urlPattern


class WatchlistParser(object):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
        watchlist = re.findall(WatchlistPattern().pattern, content)
        data_table = []
        if watchlist:
            for item in watchlist:
                url = re.findall(F95urlPattern().pattern, item)
                assert url and isinstance(url[0], str)
                url = url[0]
                data_table.append(url)
            return data_table

    @property
    def watchlist(self):
        return self.parse()
