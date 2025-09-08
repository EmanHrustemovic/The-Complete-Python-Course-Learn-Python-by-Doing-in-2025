import  re
import  logging

from ..locators.all_books_pages import AllBooksPagesLocators
from ..locators.book_locators import BookLocators

logger = logging.getLogger('scraping.all_books_page')



class BookParser:
    """
    A class to take  HTML page (or part of it), and find a property of an item in it
    """

    RATINGS = {
        'One' : 1,
        'Two' : 2,
        'Three': 3,
        'Four' : 4,
        'Five' : 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from {parent}')
        self.parent = parent

    def __repr__(self):
        return f'Book {self.name}, costing : £{self.price}, stars : {self.rating}'


    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        #locator = 'article.product_pod h3 a' #CSS Locator
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f'Found book name : {item_name}')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookLocators.LINK_LOCATOR
        #locator = 'article.product_pod h3 a' #CSS Locator
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link : {item_link}')
        return item_link

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        #locator = 'article.product_pod p.price_color'
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)' #one or more numbers and dot symbol
        matcher = re.search(pattern,item_price)
        float_price = float(matcher.group(1))#Value
        logger.debug(f'Found book price : {float_price}')
        return float_price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING_LOCATOR
        #locator = 'article.product_pod p.star-rating'
        start_rating_tags = self.parent.select_one(locator)
        classes = start_rating_tags.attrs['class'] #Give us : ['star-rating' . 'Three']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.debug(f'Found book rating : {rating_number}')
        return rating_number