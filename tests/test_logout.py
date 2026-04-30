from pages.main_page import MainPage
from pages.auth_page import AuthPage
from test_data import ExistingUser


class TestLogout:

    def test_successful_logout(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        main_page.click_login_register_button()
        auth_page.fill_login_form(ExistingUser.EMAIL, ExistingUser.PASSWORD)
        auth_page.submit_login_form()

        main_page.click_user_avatar()
        main_page.click_logout_button()

        assert main_page.is_login_register_button_displayed()
        assert not main_page.is_user_avatar_present()
