from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time


class Find3:
    
    def __init__(SELF, driver:WebDriver):
        SELF.driver = driver
        
    def find2 (SELF):

        lists = SELF.driver.find_element(By.ID, "search_results_table")

        element = lists.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

        
        for elements in element:

            title = elements.find_element(By.TAG_NAME, 'h3').text
            
            link  = elements.find_element(By.TAG_NAME, 'a').get_attribute('href')
            
            try:
                price = elements.find_element(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]').text
               
            except:
                pass
            
            try:
                price = elements.find_element(By.CSS_SELECTOR, 'div[data-testid="price-and-discounted-price"]').text
                
            except:
                pass
    
            print(title)
            print(link)
            print(price)
            print("\n") 
