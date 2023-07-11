from pages.base_page import BasePage


class ResultsPage(BasePage):
    page_url = None

    @property
    def page_title(self):
        return self.driver.title
