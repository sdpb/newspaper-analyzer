from argparse import ArgumentParser
from newspaper.utils import get_available_languages

LANGUAGE = 'en'


def arguments():
    parser = ArgumentParser()
    global LANGUAGE
    language_choices = get_available_languages()
    parser.add_argument('Newspaper',
                        help='Which newspaper do you want to analyze?',
                        type=str)
    parser.add_argument('News_items',
                        help='How many news items do you want to analyze?',
                        type=int)
    parser.add_argument('Language',
                        help='Select the newspaper original language',
                        type=str,
                        choices=language_choices)
    args = parser.parse_args()
    LANGUAGE = args.Language
    return args.Newspaper, args.News_items


def set_language(language):
    global LANGUAGE
    LANGUAGE = language
