#!/usr/bin/env python
from presentation.vars.arguments import set_origin_language, set_target_language
from presentation.visualization import results
from presentation.visualization.results import scored_news
from bussiness_logic.data_processing import filters

#from presentation.user_interface import interface

def show_news():
    for _ in filters.filtered_list:
        print(_)


def show_nonfiltered_news():
    for _ in scored_news:
        print(_)


if __name__ == '__main__':
    #newspaper_arg, n_news = arguments.arguments()
    #url = newspaper_arg
    #url = "https://www.eltiempo.com/"
    url = "https://www.nytimes.com/"
    news_number = 5
    set_origin_language('en')
    set_target_language('es')
    sentimental_type = ''
    results.execute_search(url, news_number)
    
    filters.filterNews(scored_news, sentimental_type)

    if sentimental_type == '':
        show_nonfiltered_news()
    else:
        show_news()
    
    #interface
