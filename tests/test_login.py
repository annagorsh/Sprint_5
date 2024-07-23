from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
import links

class TestLogin:
#Проверяем вход по кнопке «Войти в аккаунт» на главной
    def test_success_login_through_main(self, driver):
        driver.get(links.MAIN_URL)
        driver.find_element(*locators.LOGIN_ON_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.LOGIN_HEADER)))
        driver.find_element(*locators.LOGIN_EMAIL).send_keys("annagortester123@gmail.com")
        driver.find_element(*locators.LOGIN_PASSWORD).send_keys("Test0001")
        driver.find_element(*locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON)))
        assert (driver.current_url == links.MAIN_URL
                and (driver.find_element(*locators.PLACE_ORDER_BUTTON)).text == "Оформить заказ")
        driver.quit()

#Проверяем вход через кнопку «Личный кабинет»
    def test_success_login_through_personal_profile(self, driver):
        driver.get(links.MAIN_URL)
        driver.find_element(*locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.LOGIN_HEADER)))
        driver.find_element(*locators.LOGIN_EMAIL).send_keys("annagortester123@gmail.com")
        driver.find_element(*locators.LOGIN_PASSWORD).send_keys("Test0001")
        driver.find_element(*locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON)))
        assert (driver.current_url == links.MAIN_URL
                and (driver.find_element(*locators.PLACE_ORDER_BUTTON)).text == "Оформить заказ")
        driver.quit()

#Проверяем вход через кнопку в форме регистрации
    def test_success_login_through_regpage(self, driver):
        driver.get(links.REGISTER_URL)
        driver.find_element(*locators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.LOGIN_HEADER)))
        driver.find_element(*locators.LOGIN_EMAIL).send_keys("annagortester123@gmail.com")
        driver.find_element(*locators.LOGIN_PASSWORD).send_keys("Test0001")
        driver.find_element(*locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON)))
        assert (driver.current_url == links.MAIN_URL
                and (driver.find_element(*locators.PLACE_ORDER_BUTTON)).text == "Оформить заказ")
        driver.quit()

#Проверяем вход через кнопку в форме восстановления пароля
    def test_success_login_through_forgot_password(self, driver):
        driver.get(links.FORGOT_PASSWORD_URL)
        driver.find_element(*locators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.LOGIN_HEADER)))
        driver.find_element(*locators.LOGIN_EMAIL).send_keys("annagortester123@gmail.com")
        driver.find_element(*locators.LOGIN_PASSWORD).send_keys("Test0001")
        driver.find_element(*locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON)))
        assert (driver.current_url == links.MAIN_URL
                and (driver.find_element(*locators.PLACE_ORDER_BUTTON)).text == "Оформить заказ")
        driver.quit()
