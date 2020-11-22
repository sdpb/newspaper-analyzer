from newspaper import build
from presentation.vars import arguments


def init_newspaper(root_url):
    return build(
        root_url,
        language=arguments.ORIGIN_LANGUAGE,
        memoize_articles=False)
