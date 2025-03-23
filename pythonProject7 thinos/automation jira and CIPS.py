from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()

try:
    # Open Jira login page
    driver.get('https://jira.cpg.dell.com/login.jsp')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1erlht4')))
    # Log in
    element = driver.find_element(By.CLASS_NAME, 'css-1erlht4')
    element.click()
    username_field = driver.find_element(By.ID, "login-form-username")
    username_field.send_keys("Kirana_MS")

    password_field = driver.find_element(By.ID, "login-form-password")
    password_field.send_keys("Kiran@1808")

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@id="find_link"]')))

    issue = driver.find_element(By.XPATH,"//a[@id='find_link']")
    issue.click()


finally:
    # Close the browser
    driver.quit()



