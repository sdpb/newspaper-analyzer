from newspaper import build
from presentation.vars import arguments


def init_newspaper(root_url):
    return build(root_url, language=arguments.LANGUAGE, memoize_articles=False)
