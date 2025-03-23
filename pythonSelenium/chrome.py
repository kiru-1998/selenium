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
    driver = driver.find_element(By.NAME, 'login').click()

    # Wait for redirect after login
    WebDriverWait(driver, 10).until(EC.url_contains('dashboard'))

    # Open "Create Issue" dialog
    create_button = driver.find_element(By.ID, "create_link")
    create_button.click()

    # Wait for the dialog to appear
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "create-issue-dialog")))

    # Fill out the issue form
    project_field = driver.find_element(By.ID, "project-field")
    project_field.click()
    project_field.clear()
    project_field.send_keys("Your Project Name")
    project_field.send_keys(Keys.RETURN)

    issue_type_field = driver.find_element(By.ID, "issuetype-field")
    issue_type_field.click()
    issue_type_field.clear()
    issue_type_field.send_keys("Bug")
    issue_type_field.send_keys(Keys.RETURN)

    summary_field = driver.find_element(By.ID, "summary")
    summary_field.send_keys("Issue created by Selenium automation")

    description_field = driver.find_element(By.ID, "description")
    description_field.send_keys("This issue was automatically created by a Selenium script.")

    # Submit the issue
    submit_button = driver.find_element(By.ID, "create-issue-submit")
    submit_button.click()

    # Confirm success
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "aui-message-success")))

finally:
    # Close the browser
    driver.quit()
