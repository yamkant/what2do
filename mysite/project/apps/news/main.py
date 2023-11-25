from selenium import webdriver

from driver_helper import DriverHelper
from news_parser import NewsParser

def main():
    # Person 클래스의 인스턴스 생성
    driver = webdriver.Chrome()
    url = 'https://finance.yahoo.com/topic/stock-market-news/'
    newsParser = NewsParser(driver, url, DriverHelper(driver))
    newsParser.run()

if __name__ == "__main__":
    # main 함수 호출
    main()