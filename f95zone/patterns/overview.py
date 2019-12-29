from f95zone.patterns.base_pattern import Pattern


class OverviewPattern(Pattern):
    def __init__(self, pattern: str = r'<b>(Overview[\s\S]+?)<b>Thread'):
        Pattern.__init__(self, pattern, name='overview')
