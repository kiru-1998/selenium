from selenium import webdriver
import time
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options)
driver.maximize_window()
driver.get('https://www.youtube.com/')
search_bar = driver.find_element(By.NAME, "class="ytd-searchbox"")
search_bar.send_keys("Despacito")
search_bar.send_keys(Keys.RETURN)
