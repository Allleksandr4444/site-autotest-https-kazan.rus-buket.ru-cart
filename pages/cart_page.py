import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    checkout_button = '//*[@id="js_header-favorites__qty"]'
    cart_page = "//a[@class='sly__slides align-items-start js_product-card__slides js_product-card__link']"
    order = '//*[@id="js_btn-add-to-card"]'
    ordering = '/html/body/main/div/div/div[2]/div[1]/div[1]/button'

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_cart_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_page)))

    def get_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order)))

    def get_ordering(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ordering)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    def click_cart_page_button(self):
        self.driver.get(self.get_cart_page().get_attribute("href"))
        print("Click cart page button")

    def click_order(self):
        self.get_order().click()
        print("Click order")

    def click_ordering(self):
        self.get_ordering().click()
        print("Click ordering")

    # Methods

    def product_confirmation(self):
        self.get_current_url()
        self.click_checkout_button()
        self.click_cart_page_button()
        self.click_order()
        self.click_ordering()
