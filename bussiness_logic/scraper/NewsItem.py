from textblob import TextBlob
from presentation.vars import arguments


class NewsItem:

    def __init__(self, parsed_article):
        self.origin_language = arguments.ORIGIN_LANGUAGE
        self.target_language = arguments.TARGET_LANGUAGE
        parsed_article.download()
        parsed_article.parse()
        parsed_article.nlp()
        self.article_title = parsed_article.title
        self.article_text = parsed_article.text
        self.article_summary = parsed_article.summary
        self.article_picture = parsed_article.top_image
        obj = TextBlob(self.article_summary)
        if self.origin_language != 'en':
            obj = obj.translate(from_lang=self.origin_language, to='en')

        self.article_score = round(obj.sentiment.polarity, 3)
        self.article_subjectivity = round(obj.sentiment.subjectivity, 3)

    def __str__(self):
        return f'{self.article_title}'

    def get_title(self):
        return self.article_title

    def get_text(self):
        return self.article_text

    def get_summary(self):
        return self.article_summary

    def get_score(self):
        return self.article_score

    def get_subjectivity(self):
        return self.article_subjectivity
