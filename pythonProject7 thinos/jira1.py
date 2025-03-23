from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

# Set up WebDriver with options
chrome_options = Options()
# Uncomment this if you want to run Chrome in headless mode
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open Jira login page
    driver.get('https://jira.cpg.dell.com/browse/DTOS-22980')

    # Wait for the login button to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1erlht4')))

    # Log in
    login_button = driver.find_element(By.CLASS_NAME, 'css-1erlht4')
    login_button.click()

    # Wait for login form to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-form-username")))

    username_field = driver.find_element(By.ID, "login-form-username")
    username_field.send_keys("Kirana_MS")

    password_field = driver.find_element(By.ID, "login-form-password")
    password_field.send_keys("Kiran@1808")

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "aui-button")))

    more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "opsbar-operations_more")))
    more_button.click()

    attach_option = WebDriverWait(driver, 10).until(  EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Attach files']']")))
    attach_option.click()

    # dropdown = Select(driver.find_element(By.ID, 'opsbar-operations_more'))
    # dropdown.select_by_visible_text('Attach files')

    file_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))

    file_path = "C:/Users/Kiran/PycharmProjects/pythonProject7 thinos.log"  # Make sure to replace with your actual file path

    # Check if the file exists
    if os.path.exists(file_path):
        # Send the file path directly to the file input
        file_input.send_keys(file_path)
    else:
        print(f"File not found: {file_path}")
        driver.quit()
        exit()

    # Wait for the file to upload (adjust the class name based on your specific application)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "attachment-title")))

    print("File uploaded successfully")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
