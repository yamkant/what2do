from selenium import webdriver
import json

from classes.driver_helper import DriverHelper
from classes.news_parser import NewsParser
from classes.component_parser import PostComponentParser

def main():
    driver: webdriver = webdriver.Chrome()
    url: str = 'https://finance.yahoo.com/topic/stock-market-news/'
    driver.get(url)

    newsParser: NewsParser = NewsParser(driver, DriverHelper(driver), PostComponentParser())
    ret_json = newsParser.run()
    with open('./data/output.json', 'w', encoding='utf-8') as json_file:
        json.dump(ret_json, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()