from f95zone.patterns.base_pattern import Pattern


class DeveloperPattern(Pattern):
    def __init__(self, pattern: str = r'(<b>Developer/?(?:Publisher)?[\s\S]*?<br ?/?>)'):
        Pattern.__init__(self, pattern, name='developer')
