from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os


chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options)

try:

    driver.get('https://jira.cpg.dell.com/browse/DTOS-22980')


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1erlht4')))
    print("Login button found.")


    login_button = driver.find_element(By.CLASS_NAME, 'css-1erlht4')
    login_button.click()
    print("Clicked on login button.")

    # Wait for login form to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-form-username")))
    print("Login form appeared.")

    username_field = driver.find_element(By.ID, "login-form-username")
    username_field.send_keys("Kirana_MS")
    print("Entered username.")

    password_field = driver.find_element(By.ID, "login-form-password")
    password_field.send_keys("Kiran@1808")
    print("Entered password.")

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()
    print("Clicked on login button to submit credentials.")

    # Wait for the page to load after login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dropdown-text")))
    print("Page loaded after login.")

    # Locate and click the "More" button to reveal additional options
    more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='opsbar-operations_more']")))
    more_button.click()
    print("Clicked on 'More' button.")

    # Wait for the "Attach Files" option to be visible after clicking "More"
    attach_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Attach files']")))
    attach_option.click()
    print("Clicked on 'Attach Files' option.")

    # Locate the hidden file input element using its class or attributes
    file_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    print("File input found.")

    # Path to your file
    file_path = r"C:\Users\Kiran\PycharmProjects\pythonProject7 thinos\logs" # Replace with your actual file path
    print(f"File path: {file_path}")

    # Check if the file exists
    if os.path.exists(file_path):
        # Send the file path directly to the file input
        file_input.send_keys(file_path)
        print(f"File found and sent for upload: {file_path}")
    else:
        print(f"File not found: {file_path}")
        driver.quit()
        exit()

    # Wait for the file to upload (adjust the class name based on your specific application)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "attachment-title")))
    print("File uploaded successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
