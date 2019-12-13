import re


from f95zone.patterns.overview import OverviewPattern


class OverviewParser(object):
    """
    Overview parser
    """
    def __init__(self, overview: str):
        self._overview = overview

    def parse(self):
        overview = re.findall(OverviewPattern().pattern, self._overview)
        assert isinstance(overview, list)
        if overview:
            overview = overview[0]
            return overview

    @property
    def overview(self):
        return self.parse()
