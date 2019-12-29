import re


from f95zone.patterns.changelog import ChangelogPattern


class ChangelogParser(object):
    def __init__(self, changelog: str):
        self._changelog = changelog

    def parse(self) -> str:
        changelog: list = re.findall(ChangelogPattern().pattern, self._changelog)
        if changelog:
            changelog: str = changelog[0]
            changelog: str = re.sub(r'<.*?>', '', changelog)
            changelog: str = re.sub(r'\n{2,}', '', changelog)
            return changelog

    @property
    def changelog(self):
        return self.parse()
