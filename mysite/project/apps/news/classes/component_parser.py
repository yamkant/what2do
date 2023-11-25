from bs4 import BeautifulSoup
from pydantic import BaseModel
from typing import Optional

class PostComponent(BaseModel):
    title: Optional[str]
    published_at: Optional[str]
    author: Optional[str]
    body: Optional[str]

class PostComponentParser:
    def __init__(
        self,
    ) -> None:
        pass
    
    def set_page_source(self, page_source):
        self.page_source = page_source
        self.soup: BeautifulSoup = BeautifulSoup(page_source, 'html.parser')
    
    def get_text_in_elem(self, elem) -> str:
        return elem.text.strip() if elem else None
    
    def get_title(self) -> str:
        title_elem = self.soup.select_one('.caas-title-wrapper > h1')
        return self.get_text_in_elem(title_elem)
    
    def get_time(self) -> str:
        time_elem = self.soup.select_one('.caas-attr-time-style > time')
        return self.get_text_in_elem(time_elem)

    def get_authors(self) -> str:
        author_elem = self.soup.select_one('.caas-attr-item-author > span')
        return self.get_text_in_elem(author_elem)

    def get_body_list(self) -> str:
        post_body_list = self.soup.select('.caas-body > p')
        ret = []
        for post_body in post_body_list:
            ret.append(self.get_text_in_elem(post_body))
        return ret
    
    def get_post_compoent(self) -> PostComponent:
        ret = {
            'title': self.get_title(),
            'published_at': self.get_time(),
            'author': self.get_authors(),
            'body': ''.join(self.get_body_list()),
        }
        return PostComponent(**ret)
