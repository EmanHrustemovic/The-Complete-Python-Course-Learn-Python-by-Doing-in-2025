# LINK OF PAGE USED IN THIS PROJECT : https://quotes.toscrape.com/
from selenium import webdriver

#import requests
from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path=r"C:\Users\win11\OneDrive\Desktop\Selenium\chromedriver.exe")

#page_content = requests.get('https://quotes.toscrape.com/').content

chrome.get('https://quotes.toscrape.com/')
page = QuotesPage(chrome)

for quote in page.quotes :
    print(quote.content)

