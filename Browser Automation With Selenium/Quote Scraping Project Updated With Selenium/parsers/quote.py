from ..locators.quote_locators import QuoteLocators

class QuoteParser:
    """Given one of specific quote divs , find out data about
    the quote (quote content , author and tags).
    """
    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        return f'f<Quote {self.content}, by {self.author}'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tags(self):
        locator = QuoteLocators.TAG
        return self.parent.find_elements_by_css_selector(locator)
