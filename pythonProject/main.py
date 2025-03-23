from selenium import webdriver
import time
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options)
driver.maximize_window()
driver.get('https://www.youtube.com/')
driver.find_element(By.ID, 'search').send_keys('Music')


