from bussiness_logic.scraper.scraper import init_newspaper
from bussiness_logic.data_processing.parser import filter_articles, parse_articles
from bussiness_logic.data_processing.parser import parsed_articles

scored_news = []


def exe(newspaper_url, amount):
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
        score = _.article_score
        aux.append(_.article_title)
        aux.append(f'{round(score, 3)} {process_score(score)}')
        aux.append(f'{round(_.article_subjectivity, 3)}')
        copia = aux.copy()
        scored_news.append(copia)
        aux.clear()


def process_score(score):
    if -0.4 <= score <= 0.4:
        return 'neutral'
    elif score > 0.4:
        return 'positive'
    elif score < -0.4:
        return 'negative'
