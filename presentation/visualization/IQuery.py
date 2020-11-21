from abc import ABCMeta, abstractstaticmethod


class IQuery(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """The Query Interface"""

    @abstractstaticmethod
    def set_quantity():
        """A static inteface method"""

    @abstractstaticmethod
    def set_language():
        """A static inteface method"""

    @abstractstaticmethod
    def set_url():
        """A static inteface method"""
    
    @abstractstaticmethod
    def set_sentiment_type():
        """A static inteface method"""