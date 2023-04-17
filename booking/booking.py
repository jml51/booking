import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from booking.booking_filtration import BookingFiltration
from booking.find import Find3
from selenium.webdriver.support import expected_conditions as EC
import time

class Booking (webdriver.Chrome):
    
    def __init__(SELF, driver_path=r"C:\Program Files (x86)\chormedriver.exe", teardown=False):
        SELF.driver_path = driver_path
        SELF.teardown = teardown
        os.environ['PATH'] += SELF.driver_path
        super(Booking, SELF).__init__()
        SELF.implicitly_wait(3)
        #SELF.maximize_window()

    
    def __exit__(SELF, exc_type, exc, traceback):
        if SELF.teardown:
            SELF.quit()
        
    def cookie ( SELF):
            cookie = SELF.find_element(By.ID , "onetrust-accept-btn-handler")
            cookie.click()

    def land_first_page(SELF):
        try:
            SELF.get(const.BASE_URL)   
        except:
            print("")

        
    def change_currency(SELF, currency):

        currency_element =SELF.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Escolha a sua moeda"]')
        currency_element.click()
        
        selected_currency_element = SELF.find_element(
            By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()
        


    def select_place_to_go(SELF, place_to_go):

        try:
            element = WebDriverWait(SELF, 10).until(EC.presence_of_element_located((By.ID , ":Ra9:")))
            place= SELF.find_element(By.ID , ":Ra9:")
            place.clear()
            place.send_keys(place_to_go)
        except:   
            element = WebDriverWait(SELF, 10).until(EC.presence_of_element_located((By.ID , "ss")))
            place= SELF.find_element(By.ID , "ss")
            place.clear()
            place.send_keys(place_to_go)
        
        
        
        try:
            element = WebDriverWait(SELF, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[data-testid="autocomplete-results"]')))
            ul_select = SELF.find_element(By.CSS_SELECTOR, 'ul[data-testid="autocomplete-results"]')
            first_result = ul_select.find_element(By.CSS_SELECTOR, '#indexsearch > div.hero-banner-searchbox > div > div > form > div.ffa9856b86.db27349d3a > div:nth-child(1) > div > div > div.a7631de79e > ul > li:nth-child(2)')
            first_result.click()
        except:    
            element = WebDriverWait(SELF, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[data-i="0"]')))
            ul_select = SELF.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
            ul_select.click()



    def select_datas(SELF, check_in_date, check_out_date):

        #date = SELF.find_element(By.CSS_SELECTOR, '#indexsearch > div.hero-banner-searchbox > div > div > form > div.ffa9856b86.db27349d3a > div:nth-child(2) > div')
        #date.click()

        try:
            data_in_in = data_in.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
            data_in_in.click()
        except:    
            data_in = SELF.find_element(By.CSS_SELECTOR, 'td[class="e2f0d47913"]')
            data_in_in = data_in.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]')
            data_in_in.click()

        
        try:
            data_out = data_in.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
            data_out.click()
        except:    
            data_out = SELF.find_element(By.CSS_SELECTOR, 'td[class="e2f0d47913"]')
            data_out_in = data_in.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
            data_out_in.click()                                       

        
        
        


    def select_adults (SELF, count=2):
        try:
            adults_bt = SELF.find_element(By.ID , 'xp__guests__toggle')
            adults_bt.click()
        except:
            adults_bt = SELF.find_element(By.CSS_SELECTOR , 'button[data-testid="occupancy-config"]')
            adults_bt.click()
            

        time.sleep(2)

        while True:
            try:
                adults_decres = SELF.find_element(By.CSS_SELECTOR, 'button[class="fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 cd7aa7c891"]')
                adults_decres.click()
            except:
                adults_decres = SELF.find_element(By.CSS_SELECTOR, 'button[aria-label="Diminuir o número de Adultos"]')
                adults_decres.click()




            adults_values_elemet = SELF.find_element( By.ID , "group_adults")
            adults_values = adults_values_elemet.get_attribute("value")

        
            if int(adults_values) == 1:
                break

        try:
            adults_incres = SELF.find_element(By.CSS_SELECTOR, 'Button[aria-label="Aumentar o número de Adultos"]')
        except:
            adults_incres = SELF.find_element(By.CSS_SELECTOR, 'Button[class="fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 d64a4ea64d"]')
        
        for _ in  range(count - 1):
            adults_incres.click()




    def click_search(SELF):
        click = SELF.find_element(By.CSS_SELECTOR, 'button[type="submit"]' )
        time.sleep(10)




    def booking_filtration(SELF):
        filtration = BookingFiltration(driver = SELF)

        filtration.stars(4)
        


    def booking_find(SELF):
        filtration = Find3(driver = SELF)

        filtration.find2()
