import getpass
import requests_html


class Crawler(object):
    """
    Crawl for games in your watchlist
    """
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.session = requests_html.HTMLSession()
        self.logged_in = False

    @property
    def _api_ends(self):
        ends = {
            'url': 'https://f95zone.to',
            'watchlist': 'https://f95zone.to/watched/threads?unread=0',
            'login': 'https://f95zone.to/login'
        }
        return ends

    def login(self):
        page = self.session.get(self._api_ends['login'])
        assert isinstance(page, requests_html.HTMLResponse)
        _xftoken = page.html.find('input[name="_xfToken"]')
        assert isinstance(_xftoken, list)
        if _xftoken:
            _xftoken = _xftoken[0]
            assert isinstance(_xftoken, requests_html.Element)
            _xftoken = _xftoken.attrs['value']
        else:
            return False
        payload = {
            'login': self.__username,
            'url': '',
            'password': self.__password,
            'password_confirm': '',
            'additional_security': '',
            'remember': 1,
            '_xfRedirect': '/',
            'website_code': '',
            '_xfToken': _xftoken
        }
        post_url = f'{self._api_ends["login"]}/login'
        response = self.session.post(post_url, data=payload)
        assert isinstance(response, requests_html.HTMLResponse)
        if self.__username in response.text:
            self.logged_in = True
