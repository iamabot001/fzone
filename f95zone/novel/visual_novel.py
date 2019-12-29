import json


class VisualNovel(object):
    """
    A game
    """
    def __init__(self,
                 name: str,
                 title_tags: list,
                 tags: list,
                 overview: str,
                 version: str,
                 developer: dict,
                 url: str,
                 date: str,
                 changelog: str
                 ):
        self.name = name
        self.title_tags = title_tags
        self.tags = tags
        self.overview = overview
        self.version = version
        self.developer = developer
        self.url = url
        self.date = date
        self.changelog = changelog

    def __repr__(self):
        string = (
            f'Name: {self.name}\n'
            f'Tags: {self.title_tags}\n'
            f'Fetishes: {self.tags}\n'
            f'Overview: {self.overview}\n'
            f'Version: {self.version}\n'
            f'Developer: {self.developer}\n'
            f'Link: {self.url}\n'
            f'Thread Updates: {self.date}'
            f'Changelog: {self.changelog}'
            )
        return string

    @property
    def data(self) -> dict:
        vn_data = {
            'name': self.name,
            'title_tags': self.title_tags,
            'tags': self.tags,
            'overview': self.overview,
            'version': self.version,
            'developer': self.developer,
            'url': self.url,
            'date': self.date,
            'changelog': self.changelog
        }
        return vn_data

    @property
    def export(self):
        exportable = json.dumps(self.data, indent=4)
        return exportable
