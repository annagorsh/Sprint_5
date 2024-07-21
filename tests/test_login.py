from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

#Проверяем вход по кнопке «Войти в аккаунт» на главной
def test_success_login_through_main():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти в аккаунт')]").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Вход')]")))
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").send_keys("annagortester123@gmail.com")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").send_keys("Test0001")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()
    time.sleep(3)
    button = driver.find_element(By.XPATH, "//button[contains(.,'Оформить заказ')]")
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and button.text == "Оформить заказ"
    time.sleep(3)
    driver.quit()

#Проверяем вход через кнопку «Личный кабинет»
def test_success_login_through_personal_profile():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "(//p[@class='AppHeader_header__linkText__3q_va ml-2'])[3]").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Вход')]")))
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").send_keys("annagortester123@gmail.com")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").send_keys("Test0001")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()
    time.sleep(3)
    button = driver.find_element(By.XPATH, "//button[contains(.,'Оформить заказ')]")
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and button.text == "Оформить заказ"
    time.sleep(3)
    driver.quit()

#Проверяем вход через кнопку в форме регистрации
def test_success_login_through_regpage():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@href='/login']").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Вход')]")))
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").send_keys("annagortester123@gmail.com")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").send_keys("Test0001")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()
    time.sleep(3)
    button = driver.find_element(By.XPATH, "//button[contains(.,'Оформить заказ')]")
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and button.text == "Оформить заказ"
    time.sleep(3)
    driver.quit()

#Проверяем вход через кнопку в форме восстановления пароля
def test_success_login_through_forgot_password():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@href='/login']").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Вход')]")))
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").send_keys("annagortester123@gmail.com")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").send_keys("Test0001")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()
    time.sleep(3)
    button = driver.find_element(By.XPATH, "//button[contains(.,'Оформить заказ')]")
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and button.text == "Оформить заказ"
    time.sleep(3)
    driver.quit()
