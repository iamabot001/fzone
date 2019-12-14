import requests_html
from f95zone.paths.pathmeta import PathMeta


class Crawler(object):
    """
    Crawl for games in your watchlist
    """
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.session = requests_html.HTMLSession()
        self.logged_in = False
        self.paths = PathMeta()

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
            self.logged_in = False
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
        assertion = self.session.get(self._api_ends['url'])
        assert isinstance(assertion, requests_html.HTMLResponse)
        assertion = assertion.html.find('a[href="/account/"]>span[class="p-navgroup-linkText"]')
        assert isinstance(assertion, list)
        if assertion:
            assertion = assertion[0]
            assert isinstance(assertion, requests_html.Element)
            if self.__username in assertion.text:
                self.logged_in = True
                return True

    def get_watched(self):
        if not self.logged_in:
            assert self.login()
        content = []
        watchlist_page = self.session.get(self._api_ends['watchlist'])
        assert isinstance(watchlist_page, requests_html.HTMLResponse)
        last_page = watchlist_page.html.find('li[class="pageNav-page "]>a')
        assert isinstance(last_page, list) and last_page
        last_page = last_page[0]
        assert isinstance(last_page, requests_html.Element)
        last_page = int(last_page.text)
        urls = [f'https://f95zone.to/watched/threads?unread=0&page={x}' for x in range(2, last_page + 1)]
        urls.insert(0, self._api_ends['watchlist'])
        for url in urls:
            page = self.session.get(url)
            assert isinstance(page, requests_html.HTMLResponse)
            data = page.html.find('a[href$="unread"]')
            if data:
                for item in data:
                    temp = f'https://f95zone.to{item.attrs["href"]}'
                    content.append(temp)
        return content

    def dump(self):
        content = self.get_watched()
        with open(self.paths.cache / 'watchlist', 'w') as file:
            file.writelines((f'{x}\n' for x in content))

