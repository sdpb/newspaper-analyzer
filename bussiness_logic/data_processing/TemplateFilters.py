from abc import ABC, abstractmethod
from presentation.visualization.results import scored_news, process_score
from presentation.vars import arguments

filtered_list = []


class AbstractFilter(ABC):

    def template_filter(self):
        self.news_type = arguments.NEWS_TYPE
        self.scored_articles = scored_news
        self.filter(self.news_type, self.scored_articles)

    def filterAux(type, scored_articles):
        for _ in scored_articles:
            score = process_score(_.get_score())
            if type == score:
                filtered_list.append(_)

    # These operations have to be implemented in subclasses.

    @abstractmethod
    def filter(self, news_type, scored_articles):
        pass

'''def process_score(score):
    if -0.15 < score < 0.15:
        return 'neutral'
    elif score > 0.15:
        return 'positive'
    elif score < -0.15:
        return 'negative'''
