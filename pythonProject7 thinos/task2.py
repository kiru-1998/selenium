from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()

try:
    # Open Jira login page
    driver.get('https://jira.cpg.dell.com/login.jsp')
    driver.maximize_window()

    # Wait for the login elements to be present and then perform login
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
    issues_menu = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='find_link']")))
    # Click on "Search for issues" in the expanded menu
    search_issues = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='issues_new_search_link_lnk']")))
    search_issues.click()

    # Wait for the search page to load
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[@class='switcher-item active ']")))

    # Switch to advanced search mode
    advanced_button = WebDriverWait(driver, 30).until( EC.element_to_be_clickable((By.XPATH, "//a[@class='switcher-item active' and @data-id='basic']")))
    advanced_button.click()

    # Wait for the advanced search field to be available
    search_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='advanced-search']")))
    search_field.clear()
    search_field.send_keys('project = DTOS AND "Bug Source" in (Customer, IPS)')

    # Click the search button
    search_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']")))
    search_button.click()

    print("Search executed successfully.")

    # The browser will remain open after completing the tasks
    input("Press Enter to close the browser...")  # Keeps the browser open until you press Enter

finally:
    # Close the browser when done
    driver.quit()
