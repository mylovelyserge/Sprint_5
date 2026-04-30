from pages.main_page import MainPage
from pages.auth_page import AuthPage
from helpers import generate_email
from test_data import ExistingUser, NewUser, InvalidData


class TestRegistration:

    def test_successful_registration(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_login_register_button()
        auth_page.click_no_account_button()
        auth_page.fill_registration_form(
            email=generate_email(),
            password=NewUser.PASSWORD,
            confirm_password=NewUser.PASSWORD,
        )
        auth_page.submit_registration_form()

        assert main_page.is_user_avatar_displayed()
        assert main_page.get_user_name() == ExistingUser.NAME

    def test_registration_with_invalid_email(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_login_register_button()
        auth_page.click_no_account_button()
        auth_page.fill_registration_form(
            email=InvalidData.EMAIL,
            password=NewUser.PASSWORD,
            confirm_password=NewUser.PASSWORD,
        )
        auth_page.submit_registration_form()

        assert auth_page.is_email_error_displayed()

    def test_registration_with_existing_user(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_login_register_button()
        auth_page.click_no_account_button()
        auth_page.fill_registration_form(
            email=ExistingUser.EMAIL,
            password=ExistingUser.PASSWORD,
            confirm_password=ExistingUser.PASSWORD,
        )
        auth_page.submit_registration_form()

        assert auth_page.is_email_error_displayed()
