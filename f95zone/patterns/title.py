from f95zone.patterns.base_pattern import Pattern


class TitlePattern(Pattern):
    def __init__(self, pattern=r'\] ([^\[]+) \['):
        Pattern.__init__(self, pattern, name='title')
