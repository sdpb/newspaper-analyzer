from nltk.util import transitive_closure
from googletrans import Translator
from presentation.vars import arguments


class TranslateDecorator:

    def __init__(self, news_item):
        self.title = news_item.get_title()
        self.text = news_item.get_text()
        self.summary = news_item.get_summary()

        self.score = news_item.get_score()
        self.subjectivity = news_item.get_subjectivity()

        self.origin_language = news_item.origin_language
        self.target_language = news_item.target_language

    def __str__(self):
        return f'{self.title}'

    def get_title(self):
        text = str(self.title)
        print()
        #return text
        return translate_text(text)

    def get_text(self):
        text = self.text
        return translate_text(text)

    def get_summary(self):
        text = self.summary
        return translate_text(text)

    def get_score(self):
        return self.score

    def get_subjectivity(self):
        return self.subjectivity


def translate_text(text):
    translator = Translator()
    return translator.translate(text,src=arguments.ORIGIN_LANGUAGE,dest=arguments.TARGET_LANGUAGE).text

x = 'https://www.nytimes.com'
