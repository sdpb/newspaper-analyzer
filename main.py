#!/usr/bin/env python
from presentation.vars import arguments
from presentation.vars.arguments import set_origin_language, set_target_language, set_news_type
from presentation.visualization import results
from presentation.visualization.results import scored_news
from bussiness_logic.data_processing import TemplateFilters, filters

from presentation.user_interface import interface


def show_news():
    filters.filterNews(arguments.NEWS_TYPE)
    for _ in TemplateFilters.filtered_list:
        print(_)


def show_nonfiltered_news():
    for _ in scored_news:
        print(_)


if __name__ == '__main__':
    #newspaper_arg, n_news = arguments.arguments()
    #url = newspaper_arg
    '''
    #url = "https://www.eltiempo.com/"
    url = "https://www.nytimes.com/"
    news_number = 10
    set_origin_language('en')
    set_target_language('es')
    set_news_type('b')
    results.execute_search(url, news_number)

    if arguments.NEWS_TYPE == '':
        show_nonfiltered_news()
    else:
        show_news()
    '''
    interface
