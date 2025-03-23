from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:

    driver.get('https://jira.cpg.dell.com/login.jsp')
    driver.maximize_window()

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1erlht4')))
    element = driver.find_element(By.CLASS_NAME, 'css-1erlht4')
    element.click()

    username_field = driver.find_element(By.ID, "login-form-username")
    username_field.send_keys("Kirana_MS")

    password_field = driver.find_element(By.ID, "login-form-password")
    password_field.send_keys("Kiran@1808")

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    # Wait until the dashboard is loaded
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'dashboard')))

    # Click on the "Issues" menu
    issues_menu = WebDriverWait(driver, 80).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='find_link']"))
    )
    issues_menu.click()

    # Click on "Search for issues" in the expanded menu
    search_issues = WebDriverWait(driver, 80).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='issues_new_search_link_lnk']"))
    )
    search_issues.click()

    # Wait for the search page to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'searcher-query'))
    )

    print("Navigation to 'Search for issues' successful.")

    # Click on the "Project" dropdown
    project_dropdown = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Project: All']"))
    )
    project_dropdown.click()

    # Select "Dell ThinOS" from the dropdown
    dell_thinos_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@title='Dell ThinOS']"))
    )
    dell_thinos_option.click()

    print("Project 'Dell ThinOS' selected successfully.")

    # Click on the "More" button
    more_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='More']"))
    )
    more_button.click()

    # Select "Bug Source" from the dropdown
    bug_source_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@title='Bug Source']"))
    )
    bug_source_option.click()

    print("Bug Source selected successfully.")

    Customer_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@title='Customer']"))
    )
    Customer_option.click()

    print("customer option selected successfully.")

    IPS_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@title='IPS']"))
    )
    IPS_option.click()

    print("IPS option selected successfully.")

    search_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']"))
    )
    search_option.click()

    print("Search button selected successfully.")


finally:

    input("Press Enter to close the browser...")

