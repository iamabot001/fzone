import re


from f95zone.patterns.developer import DeveloperPattern


class DeveloperParser(object):
    def __init__(self, developer: str):
        self._developer = developer

    def parse(self) -> dict:
        data = dict()
        dev_string: list = re.findall(DeveloperPattern().pattern, self._developer)
        if dev_string:
            dev_url: str = dev_string[0]
            if 'href' in dev_url:
                dev_name: list = re.findall(r'</b> (.*?) <a', dev_url)
                if dev_name:
                    dev_name: str = dev_name[0]
                url = re.findall(r'(https://[^\s\"]+)', dev_url)
                if url:
                    url = url[0]
                else:
                    url = ''
            else:
                url = ''
                dev_name: str = re.sub('<.*?>', '', dev_url)

            data['developer'] = dev_name
            if url:
                data['url'] = url
            return data

    @property
    def developer(self):
        return self.parse()
