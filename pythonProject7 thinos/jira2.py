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


    login_button = driver.find_element(By.CLASS_NAME, 'css-1erlht4')
    login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-form-username")))

    username_field = driver.find_element(By.ID, "login-form-username")
    username_field.send_keys("Kirana_MS")

    password_field = driver.find_element(By.ID, "login-form-password")
    password_field.send_keys("Kiran@1808")

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    attach_section = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h4[@id='attachmentmodule-label']")))
    attach_section.click()
    print("Clicked on the Attachments section.")

    browse_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "attachment-browse-button")))
    print("Browse button found.")

    file_input = driver.find_element(By.XPATH, "//input[@type='file' and @class='issue-drop-zone__file ignore-inline-attach']")

    file_path = r"C:\Users\Kiran\Desktop\Device log\system_log_20240819_100329.zip"

    if os.path.exists(file_path):

        file_input.send_keys(file_path)
        print(f"File found and sent for upload: {file_path}")

        uploaded_file_name = os.path.basename(file_path)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, f"//ol[@id='attachment_thumbnails']//li[contains(., '{uploaded_file_name}')]")))
        print(f"Upload verified: {uploaded_file_name} is present on the page.")
    else:
        print(f"File not found: {file_path}")

finally:
    driver.quit()

