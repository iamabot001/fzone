import re


from f95zone.patterns.overview import OverviewPattern


class OverviewParser(object):
    """
    Overview parser
    """
    def __init__(self, overview: str):
        self._overview = overview

    def parse(self) -> str:
        overview: list = re.findall(OverviewPattern().pattern, self._overview)
        if overview:
            overview: str = overview[0]
            return overview

    @property
    def overview(self) -> str:
        return self.parse()
