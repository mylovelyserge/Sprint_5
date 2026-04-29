from pages.main_page import MainPage
from pages.auth_page import AuthPage
from test_data import (
    EXISTING_USER_EMAIL,
    EXISTING_USER_PASSWORD,
    EXISTING_USER_NAME,
)


class TestLogin:

    def test_successful_login(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_login_register_button()
        auth_page.fill_login_form(EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD)
        auth_page.submit_login_form()

        assert main_page.is_user_avatar_displayed()
        assert main_page.get_user_name() == EXISTING_USER_NAME
