from .TemplateFilters import AbstractFilter


class NegativeFilter(AbstractFilter):

    def filter(self, news_type, scored_articles):
        return AbstractFilter.filterAux(news_type, scored_articles)
