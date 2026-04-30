from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

WAIT_TIMEOUT = 10


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=WAIT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_visible(self, locator, timeout=WAIT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=WAIT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_elements(self, locator, timeout=WAIT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        for _ in range(3):
            try:
                self.wait_for_element_clickable(locator).click()
                return
            except StaleElementReferenceException:
                pass

    def type_text(self, locator, text):
        element = self.wait_for_element_clickable(locator)
        element.click()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_element_visible(locator).text

    def is_displayed(self, locator):
        return self.wait_for_element_visible(locator).is_displayed()

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click()", element)

    def wait_for_url_not_contains(self, url_part, timeout=WAIT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            lambda d: url_part not in d.current_url
        )
