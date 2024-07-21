from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

#Страница Регистрации
#Поле "Имя"
driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]")

#Поле "Email"
driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]")

#Поле "Пароль"
driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[3]")

#Информер "Некорректный пароль"
driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default'][contains(.,'Некорректный пароль')]")

#Кнопка "Зарегистрироваться"
driver.find_element(By.XPATH, "//button[contains(.,'Зарегистрироваться')]")

#Страница Логина
#Заголовок "Вход"
driver.find_element(By.XPATH, "//h2[contains(.,'Вход')]")
#Поле "Email"
driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]")

#Поле "Пароль"
driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]")

#Кнопка "Войти"
driver.find_element(By.XPATH, "//a[@href='/login']")

#Главная
#Кнопка "Войти в аккаунт"
driver.find_element(By.XPATH, "//button[contains(.,'Войти в аккаунт')]")

#Кнопка "Войти" (на разных страницах - с забытым паролем, с регистрацией)
driver.find_element(By.XPATH, "//a[@href='/login']")

#Кнопка "Личный кабинет"
driver.find_element(By.XPATH, "(//p[@class='AppHeader_header__linkText__3q_va ml-2'])[3]")

#Кнопка "Конструктор"
driver.find_element(By.XPATH, "(//a[@class='AppHeader_header__link__3D_hX'])[1]")

#Логотип Stellar Burgers
driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

#Заголовки Булки/Соусы/Начинки
driver.find_element(By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]")