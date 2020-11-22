from presentation.vars import arguments
from bussiness_logic.scraper.NewsItem import NewsItem
from .translateDecorator import TranslateDecorator
import re

parsed_articles = []


def filter_articles(raw_articles, root_url):
    re_string = r'^{}.*$'.format(root_url)
    exp = re.compile(re_string)
    filtered_articles = []
    for _ in raw_articles:
        if exp.match(_.url):
            filtered_articles.append(_)
    return filtered_articles


def parse_articles(filtered_articles):
    news_items = [NewsItem(_) for _ in filtered_articles]
    if arguments.ORIGIN_LANGUAGE != arguments.TARGET_LANGUAGE:
        news_items = [TranslateDecorator(_) for _ in news_items]
    parsed_articles.extend(news_items)
