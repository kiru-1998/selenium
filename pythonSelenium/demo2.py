from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (update the path to your ChromeDriver)
driver = webdriver.Chrome()

# Open YouTube
driver.get('https://www.youtube.com')

# Wait until the search bar is present
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'search_query'))
)

# Enter the search query and submit
search_box.send_keys('kannada music')
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'video-title'))
)

# Click on the first video in the search results
first_video = driver.find_element(By.ID, 'video-title')
first_video.click()

# Optionally, wait for the video to load and start playing
time.sleep(5)

# Close the browser
# driver.quit()
