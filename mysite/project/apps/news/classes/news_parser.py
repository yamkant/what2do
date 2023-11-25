import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from classes.driver_helper import DriverHelper
from classes.component_parser import PostComponentParser

class NewsParser:
    def __init__(
        self,
        driver,
        DriverHelper: DriverHelper,
        ComponentParser: PostComponentParser,
    ):
        self.driver: webdriver  = driver
        self.helper: DriverHelper = DriverHelper
        self.componentParser: PostComponentParser = ComponentParser

    def run(self):
        ret_json = []

        try:
            # parsing part
            titles: list[WebElement] = self.driver.find_elements(By.CLASS_NAME, 'js-content-viewer')
            print("NUMBER OF TITLES:", len(titles))
            time.sleep(3)

            for title in titles:
                try:
                    self.helper.waitForVisiableTargetInScreen(10, title)
                    title.click()
                    self.helper.waitForLoadingNewPage(10, title)

                    self.componentParser.set_page_source(self.driver.page_source)
                    ret_json.append(self.componentParser.get_post_compoent().model_dump())

                    self.driver.back()
                    time.sleep(2)

                except Exception as e:
                    # SCROLLING FOR GETTING TARGET
                    print("클릭하려는 요소가 화면에 없습니다.", e)
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", title)
                    time.sleep(1)

            return ret_json

        except Exception as e:
            print(e)
