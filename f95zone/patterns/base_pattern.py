import re


class Pattern(object):
    """
    Base pattern class
    """
    def __init__(self, pattern: str, name: str = None):
        self._pattern = pattern
        self.name = name
        self.re = re

    @staticmethod
    def make_pattern(string: str):
        pattern = re.compile(string)
        return pattern

    @property
    def pattern(self):
        return self.make_pattern(self._pattern)
