from pages.base_page import BasePage
from locators.locators import (
    LOGIN_REGISTER_BUTTON,
    PLACE_AD_BUTTON,
    USER_AVATAR,
    USER_NAME,
    LOGOUT_BUTTON,
)


class MainPage(BasePage):

    def click_login_register_button(self):
        self.click(LOGIN_REGISTER_BUTTON)

    def click_place_ad_button(self):
        self.click(PLACE_AD_BUTTON)

    def click_user_avatar(self):
        self.click(USER_AVATAR)

    def click_logout_button(self):
        self.click(LOGOUT_BUTTON)

    def get_user_name(self):
        return self.get_text(USER_NAME)

    def is_user_avatar_displayed(self):
        return self.is_displayed(USER_AVATAR)

    def is_login_register_button_displayed(self):
        return self.is_displayed(LOGIN_REGISTER_BUTTON)

    def is_user_avatar_present(self):
        return len(self.find_elements(USER_AVATAR)) > 0
