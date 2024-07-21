from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from random import randint

#Регистрация
def test_registration_success():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").send_keys("Бебебоба")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").send_keys(
        str(randint(100, 999))+"@gmail.com")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[3]").send_keys(
        str(randint(1000000, 9999999)))
    driver.find_element(By.XPATH, "//button[contains(.,'Зарегистрироваться')]").click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Вход')]")))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    time.sleep(5)
    driver.quit()


#Проверяем, что поле «Имя» должно быть не пустым;
def test_name():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").send_keys("Бебебоба")
    reg_name = driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").get_attribute("value")
    assert 0 < len(reg_name)
    time.sleep(3)
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

def test_email():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").send_keys("anna123@gmail.com")
    reg_email = driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").get_attribute("value")
    assert is_valid_email(reg_email)
    time.sleep(3)
    driver.quit()


#Проверяем, что минимальный пароль — шесть символов.
def test_password():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[3]").send_keys("password")
    reg_password = driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[3]").get_attribute("value")
    assert 6 <= len(reg_password)
    time.sleep(3)
    driver.quit()

#Проверяем появление ошибки для некорректного пароля.
def test_incorrect_password():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[3]").send_keys("12345")
    driver.find_element(By.XPATH, "//button[contains(.,'Зарегистрироваться')]").click()
    warning = driver.find_element(By.XPATH,"//p[@class='input__error text_type_main-default'][contains(.,'Некорректный пароль')]")
    assert warning.text == "Некорректный пароль"
    time.sleep(3)
    driver.quit()