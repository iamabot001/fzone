import requests_html


class Client(object):
    """
    Web client
    """
    def __init__(self):
        self.session = requests_html.HTMLSession()
        self.response_object = requests_html.HTMLResponse
        self.element_object = requests_html.Element

    def get_game_data(self, url: str):
        response = self.session.get(url)
        assert isinstance(response, self.response_object)
        title = response.html.find('h1.p-title-value')
        assert isinstance(title, list)
        if title:
            title = title[0]
            assert isinstance(title, self.element_object)
            title = title.text
            assert isinstance(title, str)
            title = title.replace(u'\xa0', u' ')
        tags = response.html.find('a.tagItem')
        assert isinstance(tags, list)
        if tags:
            temp = list()
            for item in tags:
                assert isinstance(item, self.element_object)
                temp.append(item.text)
            tags = temp
            del temp
        overview = response.html.find('div.bbWrapper')
        assert isinstance(overview, list)
        if overview:
            overview = overview[0]
            assert isinstance(overview, self.element_object)
            overview = overview.text
            assert isinstance(overview, str)
            overview = overview.replace(u'\u200b', '')

        data = {
            'title': title,
            'tags': tags,
            'overview': overview,
            'url': url
        }
        return data
