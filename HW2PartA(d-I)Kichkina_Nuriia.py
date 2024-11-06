PATH = "C:/python/chromedriver"
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re

URL = "https://www.chapters.indigo.ca/en-ca/home/kids-books-new-and-hot/\
904064-cat.html?link-usage=Header%3A%20New%20%26%20Hot&mc=Book&lu=TopNav_KidsBooks_NewHot"

browser = webdriver.Chrome(PATH)
browser.get(URL)

time.sleep(3)

content = browser.find_elements_by_css_selector(".product-list__details-left")
class BoodKids:
    name = ""
    author = ""
    price = ""

    def __init__(self, name,author,price):
        self.name = name
        self.author = author
        self.price = price

    def showDetails(self):
        print("****************************************")
        print("Book Title is: " + self.name)
        print("Author: " + self.author)
        print("Price: " + self.price)

bookList = []
for e in content:
    textContent = e.get_attribute('innerHTML')
    soup = BeautifulSoup(textContent, features="lxml")
    rawString = soup.get_text().strip()

    rawString = re.sub(r"[\n\t]*", "", rawString)

    rawString = re.sub('[ ]{2,}', '*', rawString)


    rawString = rawString.replace("Hardcover", " ")
    rawString = rawString.replace("Paperback", "*")
    rawString = rawString.replace("by", "*by")
    rawString = rawString.replace("Ba*by Shark", "Baby Shark")
    rawString = rawString.replace("list price", " ")
    rawString = rawString.replace("0$", "0*$")
    rawString = rawString.replace("5$", "5*$")
    rawString = rawString.replace("7$", "7*$")
    rawString = rawString.replace("$17.99"," ")
    rawString = rawString.replace("Picture Books", " ")
    rawString = rawString.replace("May", "*May")
    rawString = rawString.replace("March", "*March")
    rawString = rawString.replace("June", "*June")
    rawString = rawString.replace("Board Book", "")

    bookArray = rawString.split('*')

    BOOK_NAME = 0
    BOOK_AUTHOR = 1


    name = bookArray[BOOK_NAME]
    author = bookArray[BOOK_AUTHOR]
    price = bookArray[len(bookArray)-1]
    book1 = BoodKids(name,author,price)

    bookList.append(book1)

for i in range (0,len(bookList)):
    bookList[i].showDetails()


def getText(content):
    textContent = content.get_attribute('innerHTML')

    soup = BeautifulSoup(textContent, features="lxml")

    rawString = soup.get_text().strip()

    return rawString


books = browser.find_elements_by_css_selector(".product-list__product-title-link--grid")
prices = browser.find_elements_by_css_selector(".product-list__listview-price")
numBooks = len(prices)

import pandas as pd

df = pd.DataFrame(columns=["Book", "Price"])
for i in range(0, numBooks):
    book = getText(books[i])
    price = getText(prices[i])
    dictionary = {"Children Book": book, "Price": price}
    df = df.append(dictionary, ignore_index=True)


print(df)

import pandas as pd
PATH        = "C:\Python/"
CSV_FILE    = 'Childrenbooks.csv'
dataset     = {"Book":["The World Needs More Purple People","The Bad Guys Collection"], "Price":["$ 22", "$ 23"]}
dfOut       = pd.DataFrame( data = dataset)

dfOut.to_csv(PATH + CSV_FILE, sep='\t')

dfIn        = pd.read_csv(PATH + CSV_FILE, sep='\t')
print(dfIn.head(2))
print(dfIn.tail(2))



