from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DriverHelper:
    def __init__(
        self,
        driver: webdriver,
    ) -> None:
        self.driver = driver

    def getScrollHeight(self) -> None:
        self.driver.execute_script("return document.body.scrollHeight")
    
    def waitForVisiableTargetInScreen(self, waitTime, target) -> None:
        WebDriverWait(self.driver, waitTime).until(EC.visibility_of(target))

    def waitForLoadingNewPage(self, waitTime, target) -> None:
        WebDriverWait(self.driver, waitTime).until(EC.title_contains(target.text))
