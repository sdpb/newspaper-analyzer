from argparse import ArgumentParser
from newspaper.utils import get_available_languages

ORIGIN_LANGUAGE = 'es'
TARGET_LANGUAGE = 'en'


def arguments():
    parser = ArgumentParser()
    global ORIGIN_LANGUAGE
    language_choices = get_available_languages()
    parser.add_argument('Newspaper',
                        help='Which newspaper do you want to analyze?',
                        type=str)
    parser.add_argument('News_items',
                        help='How many news items do you want to analyze?',
                        type=int)
    parser.add_argument('Origin_language',
                        help='Select the newspaper original language',
                        type=str,
                        choices=language_choices)
    parser.add_argument('Target_language',
                        help='Select the newspaper target language',
                        type=str,
                        choices=language_choices)

    args = parser.parse_args()
    ORIGIN_LANGUAGE = args.Origin_language
    TARGET_LANGUAGE = args.Target_languaje
    return args.Newspaper, args.News_items


def set_origin_language(language):
    global ORIGIN_LANGUAGE
    ORIGIN_LANGUAGE = language

def set_target_language(language):
    global TARGET_LANGUAGE
    TARGET_LANGUAGE = language
