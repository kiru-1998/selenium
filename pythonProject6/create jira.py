from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# Example for Chrome
driver = webdriver.Chrome()

# Open Jira Login Page
driver.get('https://jira.cpg.dell.com/login.jsp')
#//tagname[@attribute='value']
# Find the username field and enter your username
driver.find_element()











