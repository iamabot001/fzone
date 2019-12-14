from f95zone.patterns.base_pattern import Pattern


class WatchlistPattern(Pattern):
    def __init__(self, pattern: str = r'https?:\/\/[^\s]+'):
        Pattern.__init__(self, pattern, name='watchlist')
