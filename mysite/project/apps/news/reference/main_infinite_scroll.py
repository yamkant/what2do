from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import json

class DriverHelper:
    def __init__(self, driver) -> None:
        self.driver = driver

    def getScrollHeight(self):
        return driver.execute_script("return document.body.scrollHeight")


driver = webdriver.Chrome()
url = 'https://finance.yahoo.com/topic/stock-market-news/'
driver.get(url)
response = requests.get(url)

SCROLL_PAUSE_TIME = 2


helper = DriverHelper(driver)
accHeight = driver.execute_script("return document.body.scrollHeight")
result = []
tick = 0

try:
    while tick < 5:
        scroll_script = f'window.scrollTo(0, {accHeight});'
        new_height = driver.execute_script(scroll_script)
        accHeight += helper.getScrollHeight()


        time.sleep(SCROLL_PAUSE_TIME)
        tick += 1


    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    articles = soup.find_all('h3', class_='Mb(5px)')
    for article in articles:
        title = article.text.strip()
        link = article.find('a')['href']
        result.append({'title': title, 'link': link})

    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=2)


except KeyboardInterrupt:
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=2)

# driver.quit()