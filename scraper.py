from newspaper import build, news_pool
from re import compile
from multiprocessing import Pool, Queue, Process
from argparse import ArgumentParser

# Local imports
from NewsItem import NewsItem

multiprocessing_queue = Queue()
parsed_articles = []


def init_newspaper(root_url):
    # This code is a failed implementation of multi threads by newspaper library
    """
    newspaper = build(root_url, language='es', memoize_articles=False)
    print(newspaper.size())
    news_pool.set([newspaper], threads_per_source=2)
    news_pool.join()
    return newspaper
    """
    return build(root_url, language='es', memoize_articles=False)


def filter_articles(raw_articles, root_url):
    re_string = r'^{}.*$'.format(root_url)
    exp = compile(re_string)
    filtered_articles = []
    for _ in raw_articles:
        if exp.match(_.url):
            filtered_articles.append(_)
    return filtered_articles


def parse_articles(filtered_articles):
    # Unstable implementation of multicore by multiprocessing library
    """
    i = 0
    for _ in filtered_articles:
        i += 1
        print(i)
        multiprocessing_queue.put(News(_))
    """
    parsed_articles.extend([NewsItem(_) for _ in filtered_articles])


# Unstable method
def pool_handler(function, articles):
    p = Pool(3)
    p.map(function, articles)


def multiprocessing(func, split_articles1, split_articles2, split_articles3):
    print('Creating processes')
    p1 = Process(target=func, args=(split_articles1,))
    p2 = Process(target=func, args=(split_articles2,))
    p3 = Process(target=func, args=(split_articles3,))

    print('Starting processes')
    p1.start()
    p2.start()
    p3.start()

    p1.join()
#    p2.join()
#    p3.join()

    print('Ending multiprocessing')


def show_score():
    i = 1
    for _ in parsed_articles:
        score = _.article_score
        print('{})'.format(i), _.article_title, '\nSCORE =', score, process_score(score),
              '\nSUBJECTIVITY =', _.article_subjectivity, '\n')
        i += 1


def show_score_multiprocessing():
    while not multiprocessing_queue.empty():
        _ = multiprocessing_queue.get()
        score = _.article_score
        print(_.article_title, '\nSCORE =', score, process_score(score), '\nSUBJECTIVITY =', _.article_subjectivity)


def process_score(score):
    if score == 0:
        return 'Neutral news.'
    elif score > 0:
        return 'Positive news.'
    elif score < 0:
        return 'Negative news.'


def exe(newspaper_url, amount):
    newspaper = init_newspaper(newspaper_url)
    print('{} news were found in {}.\n'.format(newspaper.size(), newspaper_url))
    filtered_articles = filter_articles(newspaper.articles[:amount], newspaper_url)
    parse_articles(filtered_articles)

    # It works with multiprocessing method
    """
    n = int(len(filtered_articles) // 3)
    multiprocessing(parse_articles, filtered_articles[:n], filtered_articles[n:2 * n],
                    filtered_articles[2 * n:3 * n])
    show_score_multiprocessing()
    """
    # pool_handler(parse_articles, filtered_articles) # Unstable method
    show_score()


def which_newspaper():
    parser = ArgumentParser()

    news_site_choices = ["eltiempo", "elcolombiano", "elpais"]
    parser.add_argument('Newspaper',
                        help='Which newspaper do you wanna analyze?',
                        type=str,
                        choices=news_site_choices)
    args = parser.parse_args()
    return args.Newspaper


def get_newspaper_url(newspaper):
    if newspaper == 'eltiempo' or 'elcolombiano':
        return 'https://www.' + newspaper + '.com/'
    elif newspaper == 'elpais':
        return 'https://' + newspaper + '.com/'


if __name__ == '__main__':
    newspaper_arg = which_newspaper()
    message = 'Due to the computational requirement, is recommended to select a little amount of news.'
    print('*' * len(message))
    print(message)
    n_news = int(input('Amount of news to analyze: '))
    print('*' * len(message), '\n')
    url = get_newspaper_url(newspaper_arg)
    exe(url, n_news)

    # unit test
    # exe('https://www.eltiempo.com/', n_news)
    # exe('https://www.elcolombiano.com/', n_news)
    # exe('https://elpais.com/', n_news)
