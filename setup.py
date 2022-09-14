from setuptools import setup

setup(
    name='coingecko-news-api',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'beautifulsoup4==4.11.1',
    ],
    packages=[
        'geckonewsapi',
    ],
)
