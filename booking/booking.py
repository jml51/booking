import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from booking.booking_filtration import BookingFiltration
from selenium.webdriver.support import expected_conditions as EC
import time

class Booking (webdriver.Chrome):
    


    
    def cookie ( SELF):
        cookie = SELF.find_element(By.ID , "onetrust-accept-btn-handler")
        cookie.click()


    def change_currency(SELF, currency):

        currency_element =SELF.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Escolha a sua moeda"]')
        currency_element.click()
        
        selected_currency_element = SELF.find_element(
            By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()
        


    def select_place_to_go(SELF, place_to_go):

        element = WebDriverWait(SELF, 100).until(EC.presence_of_element_located(
            (By.ID , ":Ra9:")))

        place= SELF.find_element(By.ID , ":Ra9:")
        place.clear()
        place.send_keys(place_to_go)

        element = WebDriverWait(SELF, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#indexsearch > div.hero-banner-searchbox > div > div > form > div.ffa9856b86.db27349d3a > div:nth-child(1) > div > div > div.a7631de79e > ul > li:nth-child(2)')))

        first_result = SELF.find_element(By.CSS_SELECTOR, '#indexsearch > div.hero-banner-searchbox > div > div > form > div.ffa9856b86.db27349d3a > div:nth-child(1) > div > div > div.a7631de79e > ul > li:nth-child(2)')
        first_result.click()



    def select_datas(SELF, check_in_date, check_out_date):

        date = SELF.find_element(By.CSS_SELECTOR, '#indexsearch > div.hero-banner-searchbox > div > div > form > div.ffa9856b86.db27349d3a > div:nth-child(2) > div')
        date.click()
        
        
        data_in = SELF.find_element(By.CSS_SELECTOR, 'td[class="e2f0d47913"]')
        data_in_in = data_in.find_element(By.CSS_SELECTOR, 'span[data-date="{check_in_date}"]')
        data_in_in.click()
        
        data_out = SELF.find_element(By.CSS_SELECTOR, 'td[class="e2f0d47913"]')
        data_out_in = data_in.find_element(By.CSS_SELECTOR, 'span[data-date="{check_out_date}"]')
        data_out_in.click()


    def select_adults (SELF, count=2):
        adults_bt = SELF.find_element(By.ID , 'xp__guests__toggle')
        adults_bt.click()

        time.sleep(2)

        while True:

            adults_decres = SELF.find_element(By.CSS_SELECTOR, 'button[aria-label="Diminuir o número de Adultos"]')
            adults_decres.click()
            

            adults_values_elemet = SELF.find_element( By.ID , "group_adults")
            adults_values = adults_values_elemet.get_attribute("value")

        
            if int(adults_values) == 1:
                break

        adults_incres = SELF.find_element(By.CSS_SELECTOR, 'Button[aria-label="Aumentar o número de Adultos"]')
        
        for _ in  range(count - 1):
            adults_incres.click()




    def click_search(SELF):
        click = SELF.find_element(By.CSS_SELECTOR, 'button[type="submit"]' )
        time.sleep(10)




    def booking_filtration(SELF):
        filtration = BookingFiltration(driver = SELF)

        filtration.stars(4)
        filtration.find2()

    def booking_find(SELF):
        filtration = Find3(driver = SELF)

        filtration.stars(4)
        filtration.find2()
