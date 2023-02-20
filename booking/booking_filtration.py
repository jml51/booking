from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    
    def __init__(SELF, driver:WebDriver):
        SELF.driver = driver
        


    def stars (SELF):
        start_filter =  SELF.driver.find_element(By.ID , "filter_group_class_:R1cq:")
        start_filter.find_element(By.ID, ":R2hl9cq:")