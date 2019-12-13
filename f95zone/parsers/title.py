import re


from f95zone.patterns.title import TitlePattern
from f95zone.patterns.tags import TagPattern


class TitleParser(object):
    """
    Parsing titles
    """
    def __init__(self, title: str):
        self._title = title

    def parse(self):
        name = re.findall(TitlePattern().pattern, self._title)
        assert isinstance(name, list)
        if name:
            name = name[0]
        tags = re.findall(TagPattern().pattern, self._title)
        assert isinstance(tags, list)
        if tags and (len(tags) > 2):
            version = tags[-2]
            developer = tags[-1]
            title_tags = tags[:-2]
        elif tags:
            version = tags[0]
            developer = tags[1]
        else:
            return
        data = {
            'name': name,
            'version': version,
            'developer': developer
        }
        if len(tags) > 2:
            data['tags'] = title_tags
            return data
        return data

    @property
    def title(self):
        return self.parse()
