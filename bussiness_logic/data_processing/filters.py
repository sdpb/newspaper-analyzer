from bussiness_logic.data_processing.neutralFilter import NeutralFilter
from bussiness_logic.data_processing.negativeFilter import NegativeFilter
from bussiness_logic.data_processing.positiveFilter import PositiveFilter
from .TemplateFilters import AbstractFilter



def filter_type(abstract_filter: AbstractFilter):
    abstract_filter.template_filter()

def filterNews(new_type):
    if new_type == 'positive':
        filter_type(PositiveFilter())

    elif new_type == 'negative':
        filter_type(NegativeFilter())
        # filterAux('negative', scored_articles)

    elif new_type == 'neutral':
        filter_type(NeutralFilter())
        # filterAux('neutral', scored_articles)


