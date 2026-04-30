class Config:
    BASE_URL = "https://qa-desk.education-services.ru/"


class ExistingUser:
    EMAIL = "mylovelyserge@gmail.com"
    PASSWORD = "qwerty123"
    NAME = "User."


class NewUser:
    PASSWORD = "Test1234!"


class InvalidData:
    EMAIL = "not-valid-email"


class AdData:
    TITLE = "Тестовое объявление"
    DESCRIPTION = "Описание тестового объявления"
    PRICE = "1000"
    CATEGORY = "Технологии"
    CITY = "Москва"
