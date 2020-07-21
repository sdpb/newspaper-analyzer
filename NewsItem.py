from textblob import TextBlob


class NewsItem:

    def __init__(self, parsed_article, lang):
        parsed_article.download()
        parsed_article.parse()
        parsed_article.nlp()
        self.article_title = parsed_article.title
        self.article_text = parsed_article.text
        self.article_summary = parsed_article.summary
        self.article_picture = parsed_article.top_image
        obj = TextBlob(parsed_article.summary)
        if lang != 'en':
            obj = obj.translate(from_lang=lang, to='en')
        self.article_score = obj.sentiment.polarity
        self.article_subjectivity = obj.sentiment.subjectivity


