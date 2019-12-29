from f95zone.patterns.base_pattern import Pattern


class ThreadDatePattern(Pattern):
    def __init__(self, pattern: str = r'(<b>Thread[\s\S]*?)<b>Developer'):
        Pattern.__init__(self, pattern, name='thread_date')
