from nltk.util import transitive_closure
from googletrans import Translator


class TranslateDecorator:

    def __init__(self, news_item):
        self.title = news_item.get_title()
        self.text = news_item.get_text()
        self.summary = news_item.get_summary()

        self.score = news_item.get_score()
        self.subjetivity = news_item.get_subjetivity()

        self.origin_language = news_item.origin_language
        self.target_language = news_item.target_language

    def get_title(self):
        text = self.title
        return translate_text(self, text)

    def get_text(self):
        text = self.text
        return translate_text(self, text)

    def get_summary(self):
        text = self.summary
        return translate_text(self, text)

    def get_score(self):
        return self.score

    def get_subjetivity(self):
        return self.subjectivity


def translate_text(self, text):
    translator = Translator()
    return translator.translate(text,
                                src=self.origin_language,
                                dest=self.target_language)

x = 'https://www.nytimes.com'
