import os
import pathlib


class PathMeta(object):
    """
    path manager
    """
    def __init__(self):
        self.package_root = pathlib.Path(__file__).parent.parent
        self.home = pathlib.Path(os.environ['HOME'])
        self._cache = self.home / '.cache' / 'f95zone'
        self.watchlist = self._cache / 'watchlist'

    @staticmethod
    def make_path(path):
        if not pathlib.Path(path).exists():
            pathlib.Path(path).mkdir(parents=True)

    @property
    def cache(self):
        self.make_path(self._cache)
        return self._cache
