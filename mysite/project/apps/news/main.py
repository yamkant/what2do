from selenium import webdriver
import json

from driver_helper import DriverHelper
from news_parser import NewsParser

def main():
    driver: webdriver = webdriver.Chrome()
    url: str = 'https://finance.yahoo.com/topic/stock-market-news/'
    newsParser: NewsParser = NewsParser(driver, url, DriverHelper(driver))
    ret_json = newsParser.run()
    with open('./data/output.json', 'w', encoding='utf-8') as json_file:
        json.dump(ret_json, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()