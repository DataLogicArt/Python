PATH = "C:/python/chromedriver"

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re


URL = "https://www.bcit.ca/"
browser = webdriver.Chrome(PATH)
browser.get(URL)

time.sleep(3)

SEARCH_TERM = "Data Analytics"
search = browser.find_element_by_css_selector("#site-header-search")

search.send_keys(SEARCH_TERM)

# Find the search button - this is only enabled when a search query is entered
button = browser.find_element_by_css_selector(".site-header__search-btn")
button.click()  # Click the button.
time.sleep(4)


pageNum = 1;
for i in range(0, 3):
    content = browser.find_elements_by_css_selector(".bcit-search-results__item")

    for e in content:
        textContent = e.get_attribute('innerHTML')
        soup = BeautifulSoup(textContent, features="lxml")
        rawString = soup.get_text().strip()
        time.sleep(3)
        print(rawString)
        print("***")




    pageNum += 1


    URL_NEXT = "https://www.bcit.ca/s/?query=" + SEARCH_TERM + "&profile=_default&collection=bcit-search&start_rank=11"
    URL_NEXT = URL_NEXT + str(pageNum)
    browser.get(URL_NEXT)

    print("Count: ", str(i))
    time.sleep(3)




print("done loop")
