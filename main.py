#!/usr/bin/env python
from presentation.vars.arguments import set_origin_language, set_target_language
from presentation.vars import arguments
from presentation.visualization import results
#from presentation.user_interface import interface

if __name__ == '__main__':
    #newspaper_arg, n_news = arguments.arguments()
    #url = newspaper_arg
    url = "https://www.eltiempo.com/"
    news_number = 5
    set_origin_language('es')
    set_target_language('en')
    results.execute_search(url, news_number)
    filters.filterNews(scored_news, sentimental_type)

    if sentimental_type == '':
        show_nonfiltered_news()
    else:
        show_news()
    #interface
