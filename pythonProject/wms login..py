
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options. add_experimental_option("detach",True)
driver = webdriver.Chrome(options)
driver.maximize_window()
driver.get('https://100.106.119.153/ccm-web/login')
driver.find_element(By.ID, "details-button").click()
driver.find_element(By.ID, "proceed-link").click()
driver.find_element(By.ID, "j_username").send_keys('kiran@dell.com')
driver.find_element(By.NAME, "j_password").send_keys("Kiru@1998")
driver.find_element(By.CLASS_NAME, "button").click()
a = driver.find_element(By.LINK_TEXT, "Groups & Configs")
a.click()