# Coingecko news API

Simple scraper for coingecko news, that parses articles

Install:
---
```sh
sudo python3 setup.py install
```

Using the API:
---
To use api just import it with:
```py
from geckonewsapi import api
```
Endpoints either return generator or list, of object `Article`

Regular article:
```
Article(
	image  = https://assets.coingecko.com/article-images/631749.jpg
	title  = Traders Flock to Binance as New Taxes Send Indian Exchanges Out of Business: Report
	url    = https://cryptopotato.com/traders-flock-to-binance-as-new-taxes-send-indian-exchanges-out-of-business-report/
	time   = 1 hour ago
	type   = regular
	source = CryptoPotato
	short  = Available data shows that Binance app downloads grew in August when all other major exchanges saw a drop.
)
```
Featured article:
```
Article(
	image  = https://static.coingecko.com/s/article_thumbnail_placeholder-d2df8de3bd02b5d7a3b717dd86f2df8a71885b5fc5a45a977e5a7a17d2645375.png
	title  = On-Chain Expert Willy Woo Says Bitcoin (BTC) Hasn’t Reached ‘Max Pain’ Just Yet – Here’s Why
	url    = https://dailyhodl.com/2022/09/14/on-chain-expert-willy-woo-says-bitcoin-btc-hasnt-reached-max-pain-just-yet-heres-why/
	time   = 13 minutes ago
	type   = featured
	source = None
	short  = None
)
```

Endpoints:
---
#### scrape_page
Get articles on page, paging starts with 1, not 0, returns list of `Article`
```py
articles = api.scrape_page(page = 1, lang = 'en')
```

#### scrape_page_iter
Returns generator, that yields `Article` for each news on that page
```py
for article in api.scrape_page_iter(page = 1, lang = 'en'):
    print(article)
```

#### scrape_pages
Returns list of every article from page 1 to page `max_page`
```py
articles = api.scrape_pages(max_page = 10, lang = 'en')
```

#### scrape_pages_iter
Returns generator of every article from page 1 to page `max_page`
```py
for article in api.scrape_pages_iter(max_page = 10, lang = 'en'):
    print(article)
```

#### scrape_pages_raw
Returns list of every article on passed pages
```py
articles = api.scrape_pages_raw(pages = [32, 6, 5, 3], lang = 'en')
```

#### scrape_pages_raw_iter
Returns generator of every article on passed pages
```py
for article in api.scrape_pages_raw_iter(pages = [32, 6, 5, 3], lang = 'en'):
    print(article)
```
