from f95zone.patterns.base_pattern import Pattern


class F95urlPattern(Pattern):
    def __init__(self, pattern: str = r'(https://f95zone\.to\/threads\/.*?)\/'):
        Pattern.__init__(self, pattern, name='f95url')
