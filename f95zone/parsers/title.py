import re
import typing


from f95zone.patterns.title import TitlePattern
from f95zone.patterns.tags import TagPattern


class TitleParser(object):
    """
    Parsing titles
    """
    def __init__(self, title: str):
        self._title = title

    def parse(self) -> dict:
        title_tags = None
        name: list = re.findall(TitlePattern().pattern, self._title)
        if name:
            name: str = name[0]
        tags: list = re.findall(TagPattern().pattern, self._title)

        if len(tags) == 1:
            data = {
                'name': '] '.split(self._title)[-1],
                'tags': tags,
                'version': 'NA',
                'developer': 'NA'
            }
            return data

        if tags and (len(tags) > 2):
            version: str = tags[-2]
            developer: str = tags[-1]
            title_tags: typing.Union[list, None] = tags[:-2]
        elif tags:
            version: str = tags[0]
            developer: str = tags[1]
        else:
            return {}
        data = {
            'name': name,
            'version': version,
            'developer': developer
        }
        if len(tags) > 2:
            if title_tags:
                data['tags'] = title_tags
                return data
        return data

    @property
    def title(self) -> dict:
        return self.parse()
