from nltk.util import transitive_closure
from googletrans import Translator
from textblob import TextBlob

from presentation.vars import arguments


class TranslateDecorator:

    def __init__(self, news_item):
        self.title = translate_text(news_item.get_title())
        self.text = translate_text(news_item.get_text())
        self.summary = translate_text(news_item.get_summary())

        self.score = news_item.get_score()
        self.subjectivity = news_item.get_subjectivity()

        self.origin_language = news_item.origin_language
        self.target_language = news_item.target_language

    def __str__(self):
        return f'{self.title}'

    def get_title(self):
        return self.title
        

    def get_text(self):
        return self.text
        #return translate_text(text)

    def get_summary(self):
        return self.summary
        #return translate_text(text)

    def get_score(self):
        return self.score

    def get_subjectivity(self):
        return self.subjectivity


def translate_text(text):
    text = TextBlob(text)
    text = text.translate(from_lang=arguments.ORIGIN_LANGUAGE, to=arguments.TARGET_LANGUAGE)
    return str(text)


