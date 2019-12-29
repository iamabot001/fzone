import typing


import requests_html
import requests
from f95zone.crawler.crawler import Crawler


class Client(object):
    """
    Web client
    """
    response_object = typing.Union[requests.Response, requests_html.HTMLResponse]

    def __init__(self, username: str = None, password: str = None):
        self.__username = username
        self.__password = password
        self.crawler = Crawler(self.__username, self.__password) if not Crawler.instances else Crawler.instances[0]
        self._prefer_login: bool = False

    @property
    def session(self):
        if (self.__username is not None) and (self.__password is not None):
            if not self.crawler.logged_in:
                assert self.crawler.login()
            session = self.crawler.session
            self._prefer_login: bool = True
        else:
            session = requests_html.HTMLSession()
        return session

    def get_game_data(self, url: str) -> dict:
        response: Client.response_object = self.session.get(url)
        title: list = response.html.find('h1.p-title-value')
        if title:
            title: requests_html.Element = title[0]
            title: str = title.text
            title: str = title.replace(u'\xa0', u' ')

        tags: list = response.html.find('a.tagItem')
        if tags:
            temp = list()
            for item in tags:
                item: requests_html.Element
                temp.append(item.text)
            tags = temp
            del temp

        overview_block: list = response.html.find('div.bbWrapper')
        if overview_block:
            overview_block: requests_html.Element = overview_block[0]
            overview_block: str = overview_block.html
            overview_block: str = overview_block.replace(u'\u200b', '')

        data = {
            'title': title,
            'tags': tags,
            'overview_block': overview_block,
            'url': url,
            'raw_html': response.html
        }
        return data
