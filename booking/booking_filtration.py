from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time


class BookingFiltration:
    
    def __init__(SELF, driver:WebDriver):
        SELF.driver = driver
        


    def stars (SELF, *num_stars):
        start_filter =  SELF.driver.find_element(By.ID , "filter_group_class_:R1cq:")
        star_child_elements = start_filter.find_elements(By.CSS_SELECTOR, '*')

        
        for num_star in num_stars:
            for star_valeu in star_child_elements:
                if str((star_valeu.get_attribute('innerHTML')).strip() == f'"{num_stars}" estrela'):
                    star_valeu.click()

