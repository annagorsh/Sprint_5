from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
import links

class TestLogout:
#Проверяем выход по кнопке «Выйти» в личном кабинете
    def test_logout_success(self, driver):
        driver.get(links.LOGIN_URL)
        driver.find_element(*locators.LOGIN_EMAIL).send_keys("annagortester123@gmail.com")
        driver.find_element(*locators.LOGIN_PASSWORD).send_keys("Test0001")
        driver.find_element(*locators.LOGIN_BUTTON).click()
        driver.find_element(*locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.PROFILE_LINK_IN_PROFILE)))
        driver.find_element(*locators.PROFILE_LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locators.LOGIN_HEADER)))
        assert driver.current_url == links.LOGIN_URL
        driver.quit()