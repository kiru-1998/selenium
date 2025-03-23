import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('https://jira.cpg.dell.com/login.jsp')
    driver.maximize_window()


    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1erlht4')))
    element = driver.find_element(By.CLASS_NAME, 'css-1erlht4')
    element.click()

    time.sleep(1)


    username_field = driver.find_element(By.ID, "login-form-username")
    username_field.send_keys("Kirana_MS")


    password_field = driver.find_element(By.ID, "login-form-password")
    password_field.send_keys("Kiran@1808")

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'dashboard')))

    time.sleep(2)

    issues_menu = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='find_link']"))
    )
    issues_menu.click()

    time.sleep(2)

    search_issues = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='issues_new_search_link_lnk']"))
    )
    search_issues.click()

    time.sleep(2)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'searcher-query'))
    )

    print("Navigation to 'Search for issues' successful.")
    time.sleep(2)  # Pause for 2 seconds

    project_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Project: All']"))
    )
    project_dropdown.click()

    time.sleep(2)

    dell_thinos_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@title='Dell ThinOS']"))
    )
    dell_thinos_option.click()

    print("Project 'Dell ThinOS' selected successfully.")
    time.sleep(2)

    more_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='More']"))
    )
    more_button.click()

    time.sleep(2)

    bug_source_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@title='Bug Source']"))
    )
    bug_source_option.click()

    print("Bug Source selected successfully.")
    time.sleep(2)

    Customer_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@title='Customer']"))
    )
    Customer_option.click()

    print("Customer option selected successfully.")
    time.sleep(2)

    # Select "IPS"
    IPS_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@title='IPS']"))
    )
    IPS_option.click()

    print("IPS option selected successfully.")
    time.sleep(2)

    search_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']"))
    )
    search_option.click()

    print("Search button selected successfully.")

finally:
    input("Press Enter to close the browser...")

