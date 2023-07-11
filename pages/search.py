from pages.base_page import BasePage
from selenium.webdriver.common.by import By

search_field = (By.NAME, 'q')

class SearchPage(BasePage):
    page_url = '/'

    def enter_search_phrase(self, phrase):
        search = self.find(search_field)
        search.send_keys(phrase)
        search.submit()
