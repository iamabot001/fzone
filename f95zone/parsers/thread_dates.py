import re

from f95zone.patterns.thread_dates import ThreadDatePattern


class ThreadDateParser(object):
    def __init__(self, thread_date: str):
        self._dates = thread_date

    def parse(self) -> str:
        dates: list = re.findall(ThreadDatePattern().pattern, self._dates)
        if dates:
            dates: str = dates[0]
            dates: str = re.sub(r'<.*?>', '', dates)
            dates: str = re.sub(r'\n{2,}', '', dates)
            return dates

    @property
    def dates(self):
        return self.parse()
