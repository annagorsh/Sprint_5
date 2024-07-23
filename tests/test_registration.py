from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from random import randint
import locators
import links

class TestRegistration:
#Регистрация
    def test_registration_success(self, driver):
        driver.get(links.REGISTER_URL)
        driver.find_element(*locators.NAME_FIELD).send_keys("Бебебоба")
        driver.find_element(*locators.EMAIL_FIELD).send_keys(str(randint(100, 999))+"@gmail.com")
        driver.find_element(*locators.PASSWORD_FIELD).send_keys(str(randint(1000000, 9999999)))
        driver.find_element(*locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.LOGIN_HEADER)))
        assert driver.current_url == links.LOGIN_URL
        driver.quit()


#Проверяем, что поле «Имя» должно быть не пустым;
    def test_name(self, driver):
        driver.get(links.REGISTER_URL)
        driver.find_element(*locators.NAME_FIELD).send_keys("Бебебоба")
        reg_name = driver.find_element(*locators.NAME_FIELD).get_attribute("value")
        assert 0 < len(reg_name)
        driver.quit()


#Проверяем, что в поле Email введён email в формате логин@домен: например, 123@ya.ru.
    def is_valid_email(email):
        parts = email.split("@")
        if len(parts) != 2:
            return False
        username = parts[0]
        if not username:
            return False
        domain = parts[1]
        if "." not in domain:
            return False
        else:
            return True

    def test_email(self, driver):
        driver.get(links.REGISTER_URL)
        driver.find_element(*locators.EMAIL_FIELD).send_keys("anna123@gmail.com")
        reg_email = driver.find_element(*locators.EMAIL_FIELD).get_attribute("value")
        assert TestRegistration.is_valid_email(reg_email)
        driver.quit()


#Проверяем, что минимальный пароль — шесть символов.
    def test_password(self, driver):
        driver.get(links.REGISTER_URL)
        driver.find_element(*locators.PASSWORD_FIELD).send_keys("password")
        reg_password = driver.find_element(*locators.PASSWORD_FIELD).get_attribute("value")
        assert 6 <= len(reg_password)
        driver.quit()

#Проверяем появление ошибки для некорректного пароля.
    def test_incorrect_password(self, driver):
        driver.get(links.REGISTER_URL)
        driver.find_element(*locators.PASSWORD_FIELD).send_keys("12345")
        driver.find_element(*locators.REGISTER_BUTTON).click()
        warning = driver.find_element(*locators.INCORRECT_PASSWORD_WARNING)
        assert warning.text == "Некорректный пароль"
        driver.quit()