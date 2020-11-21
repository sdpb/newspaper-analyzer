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
        obj = TextBlob(parsed_article.summary)
        if self.origin_language != self.target_language:
            obj = obj.translate(from_lang=self.origin_language, to=self.target_language)
        self.article_score = obj.sentiment.polarity
        self.article_subjectivity = obj.sentiment.subjectivity

    def get_title(self):
        return self.article_title

    def get_text(self):
        return self.article_text

    def get_summary(self):
        return self.article_summary

    def get_score(self):
        return self.article_score

    def get_subjetivity(self):
        return self.article_subjectivity
