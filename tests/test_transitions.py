from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import locators
import links

#Проверяем переход в личный кабинет (авторизованным пользователем)

class TestTransitions:
    def test_go_to_profile(self, driver):
        driver.get(links.LOGIN_URL)
        driver.find_element(*locators.LOGIN_EMAIL).send_keys("annagortester123@gmail.com")
        driver.find_element(*locators.LOGIN_PASSWORD).send_keys("Test0001")
        driver.find_element(*locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON)))
        driver.find_element(*locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.PROFILE_LINK_IN_PROFILE)))
        assert driver.current_url == links.PROFILE_PAGE_URL
        driver.quit()

#Проверяем переход из личного кабинета в конструктор по клику на "Конструктор"
    def test_go_to_constructor_by_name(self, driver):
        driver.get(links.LOGIN_URL)
        driver.find_element(*locators.LOGIN_EMAIL).send_keys("annagortester123@gmail.com")
        driver.find_element(*locators.LOGIN_PASSWORD).send_keys("Test0001")
        driver.find_element(*locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON)))
        driver.find_element(*locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.PROFILE_LINK_IN_PROFILE)))
        driver.find_element(*locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON)))
        assert driver.current_url == links.MAIN_URL
        driver.quit()

#Проверяем переход из личного кабинета в конструктор по клику на логотип
    def test_go_to_constructor_by_logo(self, driver):
        driver.get(links.LOGIN_URL)
        driver.find_element(*locators.LOGIN_EMAIL).send_keys("annagortester123@gmail.com")
        driver.find_element(*locators.LOGIN_PASSWORD).send_keys("Test0001")
        driver.find_element(*locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON)))
        driver.find_element(*locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.PROFILE_LINK_IN_PROFILE)))
        driver.find_element(*locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON)))
        assert driver.current_url == links.MAIN_URL
        driver.quit()

#Проверяем переходы к разделам в "Конструкторе"
    def test_go_to_buns(self, driver):
        driver.get(links.MAIN_URL)
        driver.find_element(*locators.SAUCES_BUTTON).click()
        driver.find_element(*locators.BUNS_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.BUNS_HEADER)))
        try:
            driver.find_element(*locators.BUNS_HEADER)
            print("Элемент находится вверху страницы")
        except NoSuchElementException:
            print("Элемент не найден")
        assert driver.find_element(*locators.BUNS_HEADER) is not None, "Элемент не найден"
        driver.quit()

    def test_go_to_sauces(self, driver):
        driver.get(links.MAIN_URL)
        driver.find_element(*locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][contains(.,'Соусы')]")))
        try:
            driver.find_element(*locators.SAUCES_HEADER)
            print("Элемент находится вверху страницы")
        except NoSuchElementException:
            print("Элемент не найден")
        assert driver.find_element(*locators.SAUCES_HEADER) is not None, "Элемент не найден"
        driver.quit()

    def test_go_to_fillings(self, driver):
        driver.get(links.MAIN_URL)
        driver.find_element(*locators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        (locators.FILLINGS_HEADER)))
        try:
            driver.find_element(*locators.FILLINGS_HEADER)
            print("Элемент находится вверху страницы")
        except NoSuchElementException:
            print("Элемент не найден")
        assert driver.find_element(*locators.FILLINGS_HEADER) is not None, "Элемент не найден"
        driver.quit()