
from selenium import webdriver

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

    # Wait for redirect after login

    # Open "Create Issue" dialog
    create_button = driver.find_element(By.ID, "create_link")
    create_button.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "create-issue-dialog")))

    # Fill out the issue form

    summary_field = driver.find_element(By.ID,'summary')
    summary_field.send_keys("Issue created by Selenium automation")
    # Wait for the dialog to appear
#//input[@attribute='value']
    description_field = driver.find_element(By.ID,'tinymce')
    description_field.send_keys("This issue was automatically created by a Selenium script.")




finally:
    input('press enter to continue')





