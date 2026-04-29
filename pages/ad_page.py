from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from locators.locators import (
    AD_TITLE_INPUT,
    AD_DESCRIPTION_INPUT,
    AD_PRICE_INPUT,
    AD_CATEGORY_DROPDOWN,
    AD_CITY_DROPDOWN,
    AD_PUBLISH_BUTTON,
    MODAL_TITLE,
    PROFILE_LINK,
    MY_ADS_SECTION,
    AD_IN_PROFILE,
)


class AdPage(BasePage):

    def get_modal_title_text(self):
        return self.get_text(MODAL_TITLE)

    def fill_ad_form(self, title, description, price):
        self.type_text(AD_TITLE_INPUT, title)
        self.type_text(AD_DESCRIPTION_INPUT, description)
        self.type_text(AD_PRICE_INPUT, price)

    def select_category(self, category):
        arrow = (By.XPATH, "//input[@name='category']/following-sibling::button")
        self.click(arrow)
        option = (By.XPATH, f"//input[@name='category']/ancestor::div[contains(@class,'dropDownMenu_dropMenu')][1]//button[normalize-space()='{category}']")
        self.click(option)

    def select_city(self, city):
        arrow = (By.XPATH, "//input[@name='city']/following-sibling::button")
        self.click(arrow)
        option = (By.XPATH, f"//input[@name='city']/ancestor::div[contains(@class,'dropDownMenu_dropMenu')][1]//button[normalize-space()='{city}']")
        self.click(option)

    def select_condition(self):
        element = self.wait_for_element((By.CSS_SELECTOR, "input[name='condition']"))
        self.driver.execute_script("arguments[0].click()", element)

    def submit_ad_form(self):
        self.click(AD_PUBLISH_BUTTON)
        WebDriverWait(self.driver, 10).until(
            lambda d: "/create-lisiting" not in d.current_url
        )

    def go_to_profile(self):
        self.click(PROFILE_LINK)

    def is_my_ads_section_displayed(self):
        return self.is_displayed(MY_ADS_SECTION)

    def get_ad_titles_in_profile(self):
        ad_elements = self.wait_for_elements(AD_IN_PROFILE)
        return [el.text for el in ad_elements]
