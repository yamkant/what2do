from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DriverHelper:
    def __init__(self, driver) -> None:
        self.driver = driver

    def getScrollHeight(self):
        return self.driver.execute_script("return document.body.scrollHeight")
    
    def waitForVisiableTargetInScreen(self, waitTime, target):
        WebDriverWait(self.driver, waitTime).until(EC.visibility_of(target))
        return False

    def waitForLoadingNewPage(self, waitTime, target):
        WebDriverWait(self.driver, waitTime).until(EC.title_contains(target.text))
        return False
