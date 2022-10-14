


from typing import List

from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import SeleniumBase


class HomepageNav(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '//*[@id="trades_panel1"]/article/div[1]/top-indices/table/tbody'




    def get_nav_links(self)-> List[WebElement]:
        return self.are_visible('xpath', self.__nav_links,'Navigation Links')


    def get_nav_links_text(self)->str:
        nav_links1 = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links1]
        print(nav_links_text, type(nav_links_text))
        return ','.join(nav_links_text)


