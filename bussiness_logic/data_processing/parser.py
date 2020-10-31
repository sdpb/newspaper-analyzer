from presentation.vars import arguments
from bussiness_logic.scraper.NewsItem import NewsItem
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
    parsed_articles.extend([NewsItem(_, arguments.LANGUAGE) for _ in filtered_articles])
