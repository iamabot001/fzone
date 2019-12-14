from f95zone.patterns.base_pattern import Pattern


class TagPattern(Pattern):
    def __init__(self, pattern: str = r'\[(.*?)\]'):
        Pattern.__init__(self, pattern, name='tags')
