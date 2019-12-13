import pickle
import json


from f95zone.parsers.title import TitleParser
from f95zone.parsers.overview import OverviewParser
from f95zone.parsers.watchlist import WatchlistParser
from f95zone.webclient.client import Client
from f95zone.paths.pathmeta import PathMeta
from f95zone.novel.visual_novel import VisualNovel


class Cache(object):
    def __init__(self):
        self.paths = PathMeta()
        self.client = Client()

    def generate_cache(self):
        novels = []
        watchlist = WatchlistParser(str(self.paths.watchlist)).watchlist
        for url in watchlist:
            raw_data = self.client.get_game_data(url)
            title = TitleParser(raw_data['title']).title
            overview = OverviewParser(raw_data['overview']).overview
            game = {
                'name': title['name'],
                'title_tags': title.get('tags', None),
                'tags': raw_data['tags'],
                'version': title['version'],
                'developer': title['developer'],
                'overview': overview,
                'url': url
            }
            novels.append(VisualNovel(**game))
        return novels

    def dump(self):
        data = self.generate_cache()
        with open(str(self.paths.cache / 'data0.pickle'), 'wb') as file:
            file.write(pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL))
        return True


cone = Cache()
cone.dump()
