from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.ad_page import AdPage
from test_data import ExistingUser, AdData


class TestAdCreation:

    def test_create_ad_unauthorized(self, driver):
        main_page = MainPage(driver)
        ad_page = AdPage(driver)

        main_page.click_place_ad_button()

        assert "авторизуйтесь" in ad_page.get_modal_title_text().lower()

    def test_create_ad_authorized(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)
        ad_page = AdPage(driver)

        main_page.click_login_register_button()
        auth_page.fill_login_form(ExistingUser.EMAIL, ExistingUser.PASSWORD)
        auth_page.submit_login_form()

        main_page.click_place_ad_button()
        ad_page.fill_ad_form(AdData.TITLE, AdData.DESCRIPTION, AdData.PRICE)
        ad_page.select_category(AdData.CATEGORY)
        ad_page.select_city(AdData.CITY)
        ad_page.select_condition()
        ad_page.submit_ad_form()

        ad_page.go_to_profile()

        assert ad_page.is_my_ads_section_displayed()
        assert any(AdData.TITLE in title for title in ad_page.get_ad_titles_in_profile())
