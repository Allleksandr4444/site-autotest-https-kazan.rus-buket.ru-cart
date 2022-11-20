import pytest
from selenium import webdriver

import time

from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


@pytest.mark.run(order=1)
def test_buy_product_1():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\\\Users\\allle\\PycharmProjects\\resource\\chromedriver.exe',
                              chrome_options=options)

    print('Start Test 1')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    print('Finish test 1')
    time.sleep(10)
