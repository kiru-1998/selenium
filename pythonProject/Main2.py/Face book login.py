from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time(1)


def facebook_login('Kiran146172@gmail.com', 'Kiran@1998'):
    driver_path = "C:\Users\Kiran\Downloads\chrome-win64\chrome-win64"
    driver = webdriver.Chrome("C:\Users\Kiran\Downloads\chrome-win64\chrome-win64")

    driver.get("https://www.facebook.com")
    username_field = driver.find_element("name", "kiran146172@gmail.com")
    password_field = driver.find_element("name", "Kiran@1998")
    username_field.send_keys('kiran146172@gmail.com')
    password_field.send_keys('kiran@1998')
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.quit()
