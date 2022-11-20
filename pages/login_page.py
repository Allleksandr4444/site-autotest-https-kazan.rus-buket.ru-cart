from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    url = 'https://rus-buket.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    login_button = '//*[@id="js_header-login"]'
    user_email = '//*[@id="js_login-email-or-phone"]'
    password = '//*[@id="js_form-login"]/input[2]'
    enter_button = '//*[@id="js_btn-login"]'
    main_word = '/html/body/header/div[2]/div/a[1]/b'

    # Getters

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_user_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def input_user_email(self, user_name):
        self.get_user_email().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click login enter button")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_login_button()
        self.input_user_email('allleksandr4444@mail.ru')
        self.input_password('427152')
        self.click_enter_button()
        self.assert_word(self.get_main_word(), "Доставка цветов по России и Миру")
