class VisualNovel(object):
    """
    A game
    """
    def __init__(self, name: str, title_tags: str, tags: list, overview: str, version: str, developer: str, url: str):
        self.name = name
        self.title_tags = title_tags
        self.tags = tags
        self.overview = overview
        self.version = version
        self.developer = developer
        self.url = url
