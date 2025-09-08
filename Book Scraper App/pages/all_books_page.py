import re
import  logging

from bs4 import BeautifulSoup

from ..locators.all_books_pages import AllBooksPagesLocators
from ..parsers.book_parsers import BookParser

logger = logging.getLogger('scraping.all_books_page')


class AllBooksPage:
    def __init__(self,page_content):
        logger.debug('Parsing page content with BeautifulSoup HTML parsers.')
        self.soup = BeautifulSoup(page_content,'html.parsers')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using {AllBooksPagesLocators.BOOKS} .')
        return [BookParser(e) for e in  self.soup.select(AllBooksPagesLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available... ')
        content = self.soup.select_one(AllBooksPagesLocators.PAGER).string
        logger.info(f'Found number of catalogue pages available : {content} .')
        pattern = 'Page[0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.info(f'Extracted number of pages as integer : {pages} .')
        return pages