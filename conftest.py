import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = "https://qa-desk.education-services.ru/"

# Существующий пользователь для тестов логина/логаута и создания объявления
EXISTING_USER_EMAIL = "mylovelyserge@gmail.com"
EXISTING_USER_PASSWORD = "qwerty123"
EXISTING_USER_NAME = "User."


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(0)
    chrome_driver.get(BASE_URL)
    yield chrome_driver
    chrome_driver.quit()
