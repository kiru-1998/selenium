import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME,"email").send_keys('rahulshettyacademy.com')
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234")
driver.find_element(By.ID,"exampleCheck1").click()
# xpath = //tagname[@attribute='value']
# cssselector = tagname[attribute='value']
                  #id
                  #.classname
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys('rahul')
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
message= driver.find_element(By.CLASS_NAME,"alert-success").text

print(message)
assert 'Success' in message










time.sleep(7)