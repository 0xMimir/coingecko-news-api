from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from typing import Generator
from functools import wraps
from requests import get

from .exceptions import InvalidLanguage, InvalidPage, MaxRetries
from .objects import Article

headers = {
    'authority': 'www.coingecko.com',
    'accept': 'text/html',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36',
}

class api:
    max_retries = 5

    def make_request(url:str, retries: int = 0) -> str:
        if retries >= api.max_retries:
            raise MaxRetries

        try:
            html = get(url, headers = headers)
        except ConnectionError:
            retries += 1
            return api.make_request(url, retries)

        return html.text

    def check_input(page: int, lang: str) -> None:
        if page < 1:
            raise InvalidPage(page)

        if InvalidLanguage.langs.get(lang, None) is None:
            raise InvalidLanguage(lang)

    def scrape_featured(page_soup: BeautifulSoup) -> list[Article]:
        news = []
        for elem in page_soup.findAll('div', {'class': 'featured'}):
            image = elem.find('img', {'class': 'img-fluid'}).get('src')
            time = elem.find('div', {'class': 'mb-1 text-muted'}).text
            elem = elem.find('h2', {'class': 'mb-0 news-title'})
            title = elem.text
            link = elem.find('a').get('href')
            news.append(Article(**{
                'image': image,
                'title': title,
                'time': time,
                'link': link,
                'type': 'featured'
            }))

        return news

    def scrape_page_iter(page: int = 1, lang: str = 'en') -> Generator[Article, None, None]:
        api.check_input(page, lang)
        url = f'https://www.coingecko.com/{lang}/news?page={page}'
        page_soup = BeautifulSoup(api.make_request(url), features = 'lxml')

        featured = api.scrape_featured(page_soup)
        for article in featured:
            yield article

        for article in page_soup.findAll('article'):
            image = article.find('img').get('src')
            link_ = article.find('a')
            link = link_.get('href')
            title = link_.text
            time = article.find('span', {'class': None}).text
            short = article.find('div', {'class': 'post-body'}).text.strip().replace('(Read More...)', '')
            source = article.find('span', {'class': 'font-weight-bold'}).text

            yield Article(**{
                'image': image,
                'title': title,
                'time': time,
                'link': link,
                'short': short,
                'source': source,
                'type': 'regular'
            })

    def scrape_page(page: int = 1, lang: str = 'en') -> list[Article]:
        return list(api.scrape_page_iter(page, lang))

    def scrape_pages_iter(max_page: int = 10, lang: str = 'en'):
        for page in range(1, max_page):
            for article in api.scrape_page_iter(page, lang):
                yield article

    def scrape_pages(max_page: int = 10, lang: str = 'en') -> list[Article]:
        return list(api.scrape_pages_iter(max_page, lang))

    def scrape_pages_raw_iter(pages: list[int], lang: str = 'en') -> Generator[Article, None, None]:
        for page in pages:
            for article in api.scrape_page_iter(page, lang):
                yield article

    def scrape_pages_raw(pages: list[int], lang: str = 'en') -> list[Article]:
        return list(api.scrape_pages_raw_iter(pages, lang))
