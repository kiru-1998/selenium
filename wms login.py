import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--disable-web-security')

service = Service(service = Service(r"C:\Users\Kiran\Downloads\chrome-win64\chromedriver.exe"))

driver = webdriver.Chrome(service=service,options=chrome_options)
driver.get("https://100.106.119.93/ccm-web/login")

time.sleep(20)
