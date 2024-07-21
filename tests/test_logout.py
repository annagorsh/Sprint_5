from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

#Проверяем выход по кнопке «Выйти» в личном кабинете
def test_logout_success():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").send_keys("annagortester123@gmail.com")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").send_keys("Test0001")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//p[@class='AppHeader_header__linkText__3q_va ml-2'])[3]").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href='/account/profile']")))
    driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Вход')]")))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    time.sleep(5)
    driver.quit()