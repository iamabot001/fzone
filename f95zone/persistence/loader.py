import pickle
import json


from f95zone.paths.pathmeta import PathMeta
from f95zone.novel.visual_novel import VisualNovel


class Loader(object):
    """
    Load pickled data
    """
    def __init__(self):
        self.paths = PathMeta()

    def read(self):
        with open(self.paths.cache / 'data0.pickle',  'rb') as file:
            content = file.read()
        return content

    def parse(self):
        content = self.read()
        content = pickle.loads(content)
        return content

    @property
    def content(self):
        return self.parse()

    def load_json(self):
        location = self.paths.cache / 'data0.json'
        if location.exists():
            with open(location, 'r') as file:
                data = json.loads(file.read())
            return data

    @property
    def json_friendly(self):
        vns = [x.data for x in self.content if isinstance(x, VisualNovel)]
        return vns
