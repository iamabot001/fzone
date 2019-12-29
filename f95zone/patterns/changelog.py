from f95zone.patterns.base_pattern import Pattern


class ChangelogPattern(Pattern):
    def __init__(self, pattern: str = r'(<b>Changelog:[\s\S]+?</div><br />)'):
        Pattern.__init__(self, pattern, name='changelog')
