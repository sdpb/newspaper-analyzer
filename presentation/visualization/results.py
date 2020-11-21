from bussiness_logic.scraper.scraper import init_newspaper
from bussiness_logic.data_processing.parser import filter_articles, parse_articles
from bussiness_logic.data_processing.parser import parsed_articles

scored_news = []


def execute_search(newspaper_url, amount):
    newspaper = init_newspaper(newspaper_url)
    # print('{} news were found in {}.\n'.format(newspaper.size(), newspaper_url))
    filtered_articles = filter_articles(
        newspaper.articles[:amount], newspaper_url)
    parse_articles(filtered_articles)
    # nuevo
    score_news()


def score_news():
    aux = []
    for _ in parsed_articles:
        score = _.get_score()
        aux.append(_.get_title())
        aux.append(f'{round(score, 3)} {process_score(score)}')
        aux.append(f'{round(_.get_subjectivity(), 3)}')
        copy = aux.copy()
        scored_news.append(copy)
        aux.clear()


def process_score(score):
    if -0.15 < score < 0.15:
        return 'neutral'
    elif score > 0.15:
        return 'positive'
    elif score < -0.15:
        return 'negative'
