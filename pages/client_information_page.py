from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    telephone = '// *[ @ id = "customer_phone"]'
    email = '//*[@id="customer_email"]'
    first_name = '//*[@id="customer_name"]'
    last_name = '//*[@id="fullname"]'

    # Getters
    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    # Actions
    def input_telephone(self, telephone):
        self.get_telephone().clear()
        self.get_telephone().send_keys(telephone)
        print("Input telephone")

    def input_email(self, email):
        self.get_email().clear()
        self.get_email().send_keys(email)
        print("Input email")

    def input_first_name(self, first_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    # Methods

    def input_information(self):
        self.get_current_url()
        self.input_telephone('+79276117478')
        self.input_email('aleksandr@mail.ru')
        self.input_first_name('Александр')
        self.input_last_name('Ильзидуша')
