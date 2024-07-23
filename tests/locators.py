from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

#Страница Регистрации
#Поле "Имя"
NAME_FIELD = (By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]")

#Поле "Email"
EMAIL_FIELD = (By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]")

#Поле "Пароль"
PASSWORD_FIELD = (By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[3]")

#Информер "Некорректный пароль"
INCORRECT_PASSWORD_WARNING = (By.XPATH, "//p[@class='input__error text_type_main-default'][contains(.,'Некорректный пароль')]")

#Кнопка "Зарегистрироваться"
REGISTER_BUTTON = (By.XPATH, "//button[contains(.,'Зарегистрироваться')]")

#Кнопка "Войти"
LOGIN_LINK = (By.XPATH, "//a[contains(.,'Войти')]")

#Профиль
#Кнопка "Профиль"
PROFILE_LINK_IN_PROFILE = (By.XPATH, "//a[@href='/account/profile']")

#Кнопка "Выйти"
PROFILE_LOGOUT_BUTTON = (By.XPATH, "//button[@type='button'][contains(.,'Выход')]")

#Страница Логина
#Заголовок "Вход"
LOGIN_HEADER = (By.XPATH, "//h2[contains(.,'Вход')]")
#Поле "Email"
LOGIN_EMAIL = (By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]")

#Поле "Пароль"
LOGIN_PASSWORD = (By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[2]")

#Кнопка "Войти"
LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")

#Главная
#Кнопка "Войти в аккаунт"
LOGIN_ON_MAIN = (By.XPATH, "//button[contains(.,'Войти в аккаунт')]")

#Кнопка "Личный кабинет"
PROFILE_BUTTON = (By.XPATH, "//p[contains(.,'Личный Кабинет')]")

#Кнопка "Конструктор"
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(.,'Конструктор')]")

#Логотип Stellar Burgers
LOGO = (By.XPATH, "//svg[contains(@viewBox,'0 0 290 50')]")

#Кнопка "Оформить заказ"
PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(.,'Оформить заказ')]")

#Заголовки Булки/Соусы/Начинки
BUNS_BUTTON = (By.XPATH, "(//span[contains(@class,'text text_type_main-default')])[1]")
BUNS_HEADER = (By.XPATH, "//h2[contains(.,'Булки')]")
SAUCES_BUTTON = (By.XPATH, "(//span[contains(@class,'text text_type_main-default')])[2]")
SAUCES_HEADER = (By.XPATH, "//h2[contains(.,'Соусы')]")
FILLINGS_BUTTON = (By.XPATH, "(//span[contains(@class,'text text_type_main-default')])[3]")
FILLINGS_HEADER = (By.XPATH, "//h2[contains(.,'Начинки')]")