import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(service = Service(r"C:/Users/Kiran/Downloads/chrome-win64/chromedriver.exe"))
driver =webdriver.Chrome(service=service)



# driver= webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
   if checkbox.get_attribute('value') == 'option2':
       checkbox.click()
       assert checkbox.is_selected()

radio = driver.find_element(By.XPATH,"//input[@value='radio2']").click()

time.sleep(3)