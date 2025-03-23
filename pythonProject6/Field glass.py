from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def automate_fieldglass_attendance(username, password):
    # Set up the web driver (e.g., Chrome)
    driver_path = 'C:\Users\Kiran\Downloads\chromedriver-win64 (1)\chromedriver-win64'

    try:
        # Open SAP Fieldglass login page
        driver.get('https://www.fieldglass.net')

        # Wait for the login elements to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))

        # Enter username
        username_field = driver.find_element(By.NAME, 'username')
        username_field.send_keys(username)

        # Enter password
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys(password)

        # Submit login form
        password_field.send_keys(Keys.RETURN)

        # Wait for login to complete and main page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'main-content')))

        # Navigate to the attendance/clock-in page (URL might differ)
        driver.get('https://www.fieldglass.net/attendance')

        # Wait for the attendance elements to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'attendance-button')))

        # Click the attendance button
        attendance_button = driver.find_element(By.ID, 'attendance-button')
        attendance_button.click()

        # Wait for confirmation (optional)
        time.sleep(5)

        print("Attendance marked successfully")

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    # Replace with your Fieldglass credentials
    automate_fieldglass_attendance('your-username', 'your-password')
