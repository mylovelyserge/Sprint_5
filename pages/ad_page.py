from pages.base_page import BasePage
from locators.locators import (
    AD_TITLE_INPUT,
    AD_DESCRIPTION_INPUT,
    AD_PRICE_INPUT,
    AD_CATEGORY_ARROW,
    AD_CATEGORY_OPTION,
    AD_CITY_ARROW,
    AD_CITY_OPTION,
    AD_CONDITION_RADIO,
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
        self.click(AD_CATEGORY_ARROW)
        self.click(AD_CATEGORY_OPTION(category))

    def select_city(self, city):
        self.click(AD_CITY_ARROW)
        self.click(AD_CITY_OPTION(city))

    def select_condition(self):
        element = self.wait_for_element(AD_CONDITION_RADIO)
        self.js_click(element)

    def submit_ad_form(self):
        self.click(AD_PUBLISH_BUTTON)
        self.wait_for_url_not_contains("/create-lisiting")

    def go_to_profile(self):
        self.click(PROFILE_LINK)

    def is_my_ads_section_displayed(self):
        return self.is_displayed(MY_ADS_SECTION)

    def get_ad_titles_in_profile(self):
        ad_elements = self.wait_for_elements(AD_IN_PROFILE)
        return [el.text for el in ad_elements]
