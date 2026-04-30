from selenium.webdriver.common.by import By


# Главная страница
LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
PLACE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")

# Форма авторизации
LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Войти')]")
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")

# Форма регистрации
REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
REGISTER_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword']")
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Создать аккаунт')]")

# Ошибки регистрации
REGISTER_EMAIL_ERROR = (By.CSS_SELECTOR, "span.input_span__yWPqB")
REGISTER_EMAIL_FIELD_INVALID = (By.CSS_SELECTOR, "div.input_inputError__fLUP9")

# Кнопка выхода
LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.btnSmall")

# Модальное окно (форма авторизации / регистрации)
MODAL_TITLE = (By.CSS_SELECTOR, "form.popUp_shell__LuyqR h1")

# Форма создания объявления (страница /create-lisiting)
AD_TITLE_INPUT = (By.CSS_SELECTOR, "input[name='name'][placeholder='Название']")
AD_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
AD_PRICE_INPUT = (By.XPATH, "//form[contains(@class,'createListing')]//input[@name='price']")
AD_CATEGORY_DROPDOWN = (By.CSS_SELECTOR, "input[name='category']")
AD_CATEGORY_ARROW = (By.XPATH, "//input[@name='category']/following-sibling::button")
AD_CITY_DROPDOWN = (By.CSS_SELECTOR, "input[name='city']")
AD_CITY_ARROW = (By.XPATH, "//input[@name='city']/following-sibling::button")
AD_CONDITION_RADIO = (By.CSS_SELECTOR, "input[name='condition']")
AD_PUBLISH_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Опубликовать')]")


def AD_CATEGORY_OPTION(category):
    return (By.XPATH, f"//input[@name='category']/ancestor::div[contains(@class,'dropDownMenu_dropMenu')][1]//button[normalize-space()='{category}']")


def AD_CITY_OPTION(city):
    return (By.XPATH, f"//input[@name='city']/ancestor::div[contains(@class,'dropDownMenu_dropMenu')][1]//button[normalize-space()='{city}']")

# Профиль пользователя
PROFILE_LINK = (By.CSS_SELECTOR, "button.circleSmall")
MY_ADS_SECTION = (By.XPATH, "//div[contains(@class,'profilePage_listningBlock')][.//h1[contains(text(),'Мои объявления')]]")
AD_IN_PROFILE = (By.CSS_SELECTOR, ".profilePage_listningBlock__Fi6E5 .card")
