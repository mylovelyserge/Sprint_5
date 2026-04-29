from pages.main_page import MainPage
from pages.auth_page import AuthPage
from helpers import generate_email
from test_data import (
    NEW_USER_PASSWORD,
    INVALID_EMAIL,
    EXISTING_USER_EMAIL,
    EXISTING_USER_PASSWORD,
    EXISTING_USER_NAME,
)


class TestRegistration:

    def test_successful_registration(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_login_register_button()
        auth_page.click_no_account_button()
        auth_page.fill_registration_form(
            email=generate_email(),
            password=NEW_USER_PASSWORD,
            confirm_password=NEW_USER_PASSWORD,
        )
        auth_page.submit_registration_form()

        assert main_page.is_user_avatar_displayed()
        assert main_page.get_user_name() == EXISTING_USER_NAME

    def test_registration_with_invalid_email(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_login_register_button()
        auth_page.click_no_account_button()
        auth_page.fill_registration_form(
            email=INVALID_EMAIL,
            password=NEW_USER_PASSWORD,
            confirm_password=NEW_USER_PASSWORD,
        )
        auth_page.submit_registration_form()

        assert auth_page.is_email_error_displayed()

    def test_registration_with_existing_user(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_login_register_button()
        auth_page.click_no_account_button()
        auth_page.fill_registration_form(
            email=EXISTING_USER_EMAIL,
            password=EXISTING_USER_PASSWORD,
            confirm_password=EXISTING_USER_PASSWORD,
        )
        auth_page.submit_registration_form()

        assert auth_page.is_email_error_displayed()
