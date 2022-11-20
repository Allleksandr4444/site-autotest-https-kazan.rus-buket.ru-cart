import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    city_selection = '//*[@id="js_header-top"]/div/button[1]'
    city = '//*[@id="js_modal-city-search__cities"]/div/div[5]'
    search_button = '//*[@id="js_header-middle__field-search"]'
    select_product_1 = '//button[@id="js_header-middle__btn-catalog"]'
    popular = '/html/body/main/div[4]/div/div[1]/div[2]/div/div/div[1]'

    # Getters
    def get_city_selection(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_selection)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_popular(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.popular)))

    # Actions

    def click_city_selection(self):
        self.get_city_selection().click()
        print("Click city selection")

    def click_city(self):
        self.get_city().click()
        print("Click city")

    def input_search_button(self, product):
        time.sleep(1)
        self.get_search_button().send_keys(product)
        self.get_search_button().send_keys(Keys.RETURN)
        print("Input search button")

    def click_popular(self):
        time.sleep(1)
        self.get_popular().click()
        print("Click popular")

    # Methods

    def select_products_1(self):
        self.get_current_url()
        self.click_city_selection()
        self.click_city()
        self.input_search_button('розы')
        self.click_popular()
