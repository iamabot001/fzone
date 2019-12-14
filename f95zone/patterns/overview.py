from f95zone.patterns.base_pattern import Pattern


class OverviewPattern(Pattern):
    def __init__(self, pattern: str = r'Overview:(?:.*?|\s?)+(?:Developer)/?(?:Publisher)?: .*\n'):
        Pattern.__init__(self, pattern, name='overview')
