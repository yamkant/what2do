from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

class DriverHelper:
    def __init__(self, driver) -> None:
        self.driver = driver

    def getScrollHeight(self):
        return driver.execute_script("return document.body.scrollHeight")

class PostComponent:
    def __init__(self, page_source) -> None:
        self.soup = BeautifulSoup(page_source, 'html.parser')
    
    def get_text_in_elem(self, elem):
        return elem.text.strip() if elem else None
    
    def get_title(self):
        title_elem = self.soup.select_one('.caas-title-wrapper > h1')
        return self.get_text_in_elem(title_elem)
    
    def get_time(self):
        time_elem = self.soup.select_one('.caas-attr-time-style > time')
        return self.get_text_in_elem(time_elem)

    def get_authors(self):
        author_elem = self.soup.select_one('.caas-attr-item-author > .caas-author-byline-collapse')
        return self.get_text_in_elem(author_elem)

    def get_body_list(self):
        post_body_list = self.soup.select('.caas-body > p')
        ret = []
        for post_body in post_body_list:
            ret.append(self.get_text_in_elem(post_body))
        return ret
    
    def get_post_infos(self):
        ret = {
            'title': self.get_title(),
            'time': self.get_time(),
            'authors': self.get_authors(),
            'body': self.get_body_list(),
        }
        return ret


driver = webdriver.Chrome()
url = 'https://finance.yahoo.com/topic/stock-market-news/'
driver.get(url)
response = requests.get(url)
news_contents = []

try:
    titles = driver.find_elements(By.CLASS_NAME, 'js-content-viewer')

    for title in titles:
        post = {"body": []}

        title.click()
        WebDriverWait(driver, 15).until(EC.title_contains(title.text))

        internal_page_source = driver.page_source
        postcomponent = PostComponent(internal_page_source)
        news_contents.append(postcomponent.get_post_infos())
        
        driver.back()
        WebDriverWait(driver, 10).until(EC.title_contains('Latest Stock Market News'))

    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(news_contents, json_file, ensure_ascii=False, indent=2)


except Exception as e:
    print(e)
