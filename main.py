from engine import scrapper
from navigator import fileHandler
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome
import time

DRIVER_PATH = "./driver/chromedriver"
service = chrome(DRIVER_PATH)
driver = webdriver.Chrome(service=service)

if __name__ == "__main__":
  scrapper.execute_scrapper(driver)
  states_list = fileHandler.return_list_from_file("./States/state_list.json")
   
  while states_list:
    time.sleep(3)
    scrapper.execute_scrapper(driver)

  driver.quit()
  
