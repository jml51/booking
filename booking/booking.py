import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Booking (webdriver.Chrome):
    def __init__(SELF, driver_path=r"C:\Program Files (x86)\chormedriver.exe", teardown=False):
        SELF.driver_path = driver_path
        SELF.teardown = teardown
        os.environ['PATH'] += SELF.driver_path
        super(Booking, SELF).__init__()
        SELF.implicitly_wait(3)
        SELF.maximize_window()

    def __exit__(SELF, exc_type, exc, traceback):
        if SELF.teardown:
            SELF.quit()
        
    def land_first_page(SELF):
        SELF.get(const.BASE_URL)   

    def change_currency(SELF, currency):

        currency_element =SELF.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Escolha a sua moeda"]')
        currency_element.click()
        
        selected_currency_element = SELF.find_element(
            By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()
        


    def select_place_to_go(SELF, place_to_go):
        place= SELF.find_element(By.NAME, 'ss')
        place.clear()
        place.send_keys(place_to_go)

        first_result = SELF.find_element(
            By.CSS_SELECTOR, '#indexsearch > div.hero-banner-searchbox > div > div > div > form > div.ffa9856b86.db27349d3a > div:nth-child(1) > div > div > div.a7631de79e > ul > li:nth-child(1) > div')
        first_result.click()

        time.sleep(10)



















