# LINK OF PAGE USED IN THIS PROJECT : https://quotes.toscrape.com/
from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

from pages.quotes_page import QuotesPage

from selenium import webdriver

#import requests
try :
    author = input("Please choose the author : ")
    tag = input("Enter the tag : ")

    chrome = webdriver.Chrome(executable_path=r"C:\Users\win11\OneDrive\Desktop\Selenium\chromedriver.exe")
    chrome.get_sinks('https://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author,tag))

except InvalidTagForAuthorError as e :
    print(e)

except Exception as e :
    print(e)
    print("An unknown error occured. Please try again.")