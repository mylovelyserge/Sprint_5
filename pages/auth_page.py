from pages.base_page import BasePage
from locators.locators import (
    NO_ACCOUNT_BUTTON,
    REGISTER_EMAIL_INPUT,
    REGISTER_PASSWORD_INPUT,
    REGISTER_CONFIRM_PASSWORD_INPUT,
    REGISTER_SUBMIT_BUTTON,
    REGISTER_EMAIL_ERROR,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_SUBMIT_BUTTON,
)


class AuthPage(BasePage):

    def click_no_account_button(self):
        self.click(NO_ACCOUNT_BUTTON)

    def fill_registration_form(self, email, password, confirm_password):
        self.type_text(REGISTER_EMAIL_INPUT, email)
        self.type_text(REGISTER_PASSWORD_INPUT, password)
        self.type_text(REGISTER_CONFIRM_PASSWORD_INPUT, confirm_password)

    def submit_registration_form(self):
        self.click(REGISTER_SUBMIT_BUTTON)

    def get_email_error_text(self):
        return self.get_text(REGISTER_EMAIL_ERROR)

    def is_email_error_displayed(self):
        return self.is_displayed(REGISTER_EMAIL_ERROR)

    def fill_login_form(self, email, password):
        self.type_text(LOGIN_EMAIL_INPUT, email)
        self.type_text(LOGIN_PASSWORD_INPUT, password)

    def submit_login_form(self):
        self.click(LOGIN_SUBMIT_BUTTON)
