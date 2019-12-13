import pickle


from f95zone.paths.pathmeta import PathMeta


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
