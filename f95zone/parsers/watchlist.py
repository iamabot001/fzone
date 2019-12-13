import re


from f95zone.patterns.watchlist import WatchlistPattern


class WatchlistParser(object):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
        watchlist = re.findall(WatchlistPattern().pattern, content)
        if watchlist:
            return watchlist

    @property
    def watchlist(self):
        return self.parse()
