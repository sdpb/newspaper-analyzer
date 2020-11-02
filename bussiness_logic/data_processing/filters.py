filtered_list = []


def filterNews(scored_articles, new_type):
    if new_type == 'b':
        filterAux('positive', scored_articles)

    elif new_type == 'm':
        filterAux('negative', scored_articles)

    elif new_type == 'n':
        filterAux('neutral', scored_articles)


def filterAux(type, scored_articles):
    for _ in scored_articles:
        if type in _[1]:
            filtered_list.append(_)
