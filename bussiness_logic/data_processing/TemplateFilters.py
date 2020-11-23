from abc import ABC, abstractmethod
from presentation.visualization.results import scored_news
from presentation.vars import arguments

filtered_list = []


class AbstractFilter(ABC):

    def template_filter(self):
        self.news_type = arguments.NEWS_TYPE
        self.scored_articles = scored_news
        self.filter(self.news_type, self.scored_articles)

    def filterAux(type, scored_articles):
        for _ in scored_articles:
            if type in _[1]:
                filtered_list.append(_)

    # These operations have to be implemented in subclasses.

    @abstractmethod
    def filter(self, news_type, scored_articles):
        pass
