import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_button:
    def test_button_add_to_cart(self, browser):
        browser.implicitly_wait(5)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = browser.find_elements_by_css_selector(".add-to-basket>button")
        time.sleep(15)
        assert button, "No button 'add to cart' at page"

