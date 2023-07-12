import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('user-data-dir=avby-test')
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver
