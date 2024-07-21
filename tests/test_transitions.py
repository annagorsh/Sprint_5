from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time

#Проверяем переход в личный кабинет (авторизованным пользователем)
def test_go_to_profile():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").send_keys("annagortester123@gmail.com")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").send_keys("Test0001")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//p[@class='AppHeader_header__linkText__3q_va ml-2'])[3]").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href='/account/profile']")))
    time.sleep(3)
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
    driver.quit()

#Проверяем переход из личного кабинета в конструктор по клику на "Конструктор"
def test_go_to_constructor_by_name():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").send_keys("annagortester123@gmail.com")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").send_keys("Test0001")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//p[@class='AppHeader_header__linkText__3q_va ml-2'])[3]").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href='/account/profile']")))
    driver.find_element(By.XPATH, "(//a[@class='AppHeader_header__link__3D_hX'])[1]").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(.,'Соберите бургер')]")))
    time.sleep(3)
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()

#Проверяем переход из личного кабинета в конструктор по клику на логотип
def test_go_to_constructor_by_logo():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]").send_keys("annagortester123@gmail.com")
    driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]").send_keys("Test0001")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//p[@class='AppHeader_header__linkText__3q_va ml-2'])[3]").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href='/account/profile']")))
    driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(.,'Соберите бургер')]")))
    time.sleep(3)
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()

#Проверяем переходы к разделам в "Конструкторе"
def test_go_to_buns():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "(//span[@class='text text_type_main-default'])[2]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "(//span[@class='text text_type_main-default'])[1]").click()
    time.sleep(5)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][contains(.,'Булки')]")))
    try:
        element = driver.find_element(By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][contains(.,'Булки')]")
        print("Элемент находится вверху страницы")
    except NoSuchElementException:
        print("Элемент не найден")
    assert element is not None, "Элемент не найден"
    driver.quit()

def test_go_to_sauces():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "(//span[@class='text text_type_main-default'])[2]").click()
    time.sleep(5)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][contains(.,'Соусы')]")))
    try:
        element = driver.find_element(By.XPATH,
                                      "//h2[@class='text text_type_main-medium mb-6 mt-10'][contains(.,'Соусы')]")
        print("Элемент находится вверху страницы")
    except NoSuchElementException:
        print("Элемент не найден")
    assert element is not None, "Элемент не найден"
    driver.quit()

def test_go_to_fillings():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "(//span[@class='text text_type_main-default'])[3]").click()
    time.sleep(5)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][contains(.,'Начинки')]")))
    try:
        element = driver.find_element(By.XPATH,
                                      "//h2[@class='text text_type_main-medium mb-6 mt-10'][contains(.,'Начинки')]")
        print("Элемент находится вверху страницы")
    except NoSuchElementException:
        print("Элемент не найден")
    assert element is not None, "Элемент не найден"
    driver.quit()