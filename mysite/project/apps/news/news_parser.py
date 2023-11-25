import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

class PostComponentParser:
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
    
    def get_total_infos(self):
        ret = {
            'title': self.get_title(),
            'time': self.get_time(),
            'authors': self.get_authors(),
            'body': self.get_body_list(),
        }
        return ret

class NewsParser:
    def __init__(self, driver, news_url, DriverHelper):
        self.news_url = news_url
        self.driver = driver
        self.helper = DriverHelper

    def run(self):
        self.driver.get(self.news_url)
        ret_json = []

        try:
            # parsing part
            titles = self.driver.find_elements(By.CLASS_NAME, 'js-content-viewer')
            print("TITLE LENGTH:", len(titles))
            time.sleep(3)
            for title in titles:
                try:
                    # CLICKING TITLE
                    self.helper.waitForVisiableTargetInScreen(10, title)
                    print("클릭하려는 요소가 화면에 있습니다.", ", title: ", title.text)
                    title.click()
                    self.helper.waitForLoadingNewPage(10, title)

                    componentParser = PostComponentParser(self.driver.page_source)
                    ret_json.append(componentParser.get_total_infos())
                    
                    self.driver.back()
                    self.helper.waitForLoadingNewPage(10, self.driver.title)

                except Exception as e:
                    # SCROLLING FOR GETTING TARGET
                    print("클릭하려는 요소가 화면에 없습니다.")
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", title)
                    time.sleep(1)

            return ret_json


        except Exception as e:
            print(e)
