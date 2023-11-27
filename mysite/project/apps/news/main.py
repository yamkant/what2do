from selenium import webdriver
from screeninfo import get_monitors
import json

from classes.driver_helper import DriverHelper
from classes.news_parser import NewsParser
from classes.component_parser import PostComponentParser

def main():
    driver: webdriver = webdriver.Chrome()
    url: str = 'https://finance.yahoo.com/topic/stock-market-news/'


    try:
        # 현재 사용자 모니터의 해상도 정보 가져오기
        monitors = get_monitors()
        if monitors:
            monitor = monitors[0]
            width, height = monitor.width // 2, monitor.height

            driver.set_window_size(width, height)
            driver.get(url)
            newsParser: NewsParser = NewsParser(driver, DriverHelper(driver), PostComponentParser())
            ret_json = newsParser.run()
            with open('./data/output.json', 'w', encoding='utf-8') as json_file:
                json.dump(ret_json, json_file, ensure_ascii=False, indent=2)
        else:
            print("모니터 정보를 가져올 수 없습니다.")

    finally:
        # 브라우저 종료
        driver.quit()

if __name__ == "__main__":
    main()