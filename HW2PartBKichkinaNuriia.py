import time
from selenium import webdriver
from bs4 import BeautifulSoup
PATH = "C:/python/chromedriver"
URL = "https://www.theweathernetwork.com/ca/weather/british-columbia/coquitlam"

browser = webdriver.Chrome(PATH)
browser.get(URL)

time.sleep(40)
x = browser.find_elements_by_css_selector(".date")
for e in x:
    start = e.get_attribute('innerHTML')
    soup = BeautifulSoup(start, features="lxml")
    print("Day " + soup.get_text())
    print("***")


temps    = browser.find_elements_by_css_selector(".wxperiod_temp")
for e in temps:
    start = e.get_attribute('innerHTML')
    soup = BeautifulSoup(start, features="lxml")
    print(soup.get_text())
    print("***")
import matplotlib.pyplot as plt
x =  ['06/27','06/28','06/29','06/30','07/01','07/02','07/03']
tem = [17,21,23,19,19,21,22]
plt.bar(x, tem, color='green')
plt.xlabel("Day")
plt.ylabel("Tempreture")
plt.title("Coquitlam tempreture")

plt.xticks(x, x)
plt.show()
