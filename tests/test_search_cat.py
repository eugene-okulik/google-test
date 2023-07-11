from pages.search import SearchPage
from pages.results import ResultsPage


def test_cat_search(driver):
    search_page = SearchPage(driver)
    search_page.open_page()
    search_page.enter_search_phrase('cat')
    results_page = ResultsPage(driver)
    assert results_page.page_title.startswith('cat')
