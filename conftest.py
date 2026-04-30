import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_data import Config


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(0)
    chrome_driver.get(Config.BASE_URL)
    yield chrome_driver
    chrome_driver.quit()
