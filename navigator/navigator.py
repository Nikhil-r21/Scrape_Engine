import os
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from navigator import fileHandler
import time


def navigation(EX_FILE: str,BASE_URL: str,driver:WebDriver,class_name):
        # Navigate to the desired web page

    if not os.path.isfile(EX_FILE):
        driver.get(BASE_URL)
        element_list = []
        
        if "field" in EX_FILE:
            element_list = driver.find_elements(By.LINK_TEXT, "JSON")
            return element_list
            
        element_list = driver.find_elements(By.CLASS_NAME, class_name)
        state_list = []
        for el in element_list:
            state = el.text.split("\n")
            state_list.append(state[0])
           
        fileHandler.write_to_file(EX_FILE,state_list)
        
    else:
        fileHandler.read_from_file(EX_FILE)
       

def pre_data_extractor(element,driver):
    element.click()
    pre = driver.find_element(By.TAG_NAME,"pre")
    information = pre.text
    data = json.loads(information)
    return data


def navigate_if_missing(file, base_url, driver, class_name):
    """Navigates and stores data if the file does not exist."""
    navigation(EX_FILE=file, BASE_URL=base_url, driver=driver, class_name=class_name)