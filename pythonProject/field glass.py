from selenium import webdriver
import time
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options)
driver.maximize_window()
driver.get('https://Gmail.com')
driver.find_element(By.ID, "details-button").click()
driver.find_element(By.ID,"").click()
driver.find_element(By.ID,"Email").send_keys("kiran146172@gmail.com")
10
