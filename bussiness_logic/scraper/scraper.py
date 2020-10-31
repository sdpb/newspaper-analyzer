from newspaper import build
from newspaper.utils import get_available_languages
from re import compile
from argparse import ArgumentParser

# Local imports
from NewsItem import NewsItem

parsed_articles = []
LANGUAGE = 'en'


def init_newspaper(root_url):
    return build(root_url, language=LANGUAGE, memoize_articles=False)


def filter_articles(raw_articles, root_url):
    re_string = r'^{}.*$'.format(root_url)
    exp = compile(re_string)
    filtered_articles = []
    for _ in raw_articles:
        if exp.match(_.url):
            filtered_articles.append(_)
    return filtered_articles


def parse_articles(filtered_articles):
    parsed_articles.extend([NewsItem(_, LANGUAGE) for _ in filtered_articles])


def show_score():
    i = 1
    for _ in parsed_articles:
        score = _.article_score
        print('{}) {} \nSCORE = {} {}\nSUBJECTIVITY = {}'.format(
            i, _.article_title,
            round(score, 3), process_score(score),
            round(_.article_subjectivity, 3), '\n'))
        i += 1


def process_score(score):
    if -0.4 <= score <= 0.4:
        return 'Neutral news.'
    elif score > 0.4:
        return 'Positive news.'
    elif score < 0.4:
        return 'Negative news.'


def exe(newspaper_url, amount):
    newspaper = init_newspaper(newspaper_url)
    print('{} news were found in {}.\n'.format(newspaper.size(), newspaper_url))
    filtered_articles = filter_articles(
        newspaper.articles[:amount], newspaper_url)
    parse_articles(filtered_articles)

    show_score()


def arguments():
    parser = ArgumentParser()
    global LANGUAGE
    language_choices = get_available_languages()
    parser.add_argument('Newspaper',
                        help='Which newspaper do you want to analyze?',
                        type=str)
    parser.add_argument('News_items',
                        help='How many news items do you want to analyze?',
                        type=int)
    parser.add_argument('Language',
                        help='Select the newspaper original language',
                        type=str,
                        choices=language_choices)
    args = parser.parse_args()
    LANGUAGE = args.Language
    return args.Newspaper, args.News_items


if __name__ == '__main__':
    newspaper_arg, n_news = arguments()
    url = newspaper_arg
    exe(url, n_news)
