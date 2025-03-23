import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Function to perform the search and check statuses
def search_jira(driver, search_terms):
    for term in search_terms:
        search_box = driver.find_element(By.ID, 'quickSearchInput')  # Replace with actual ID of the search box
        search_box.clear()  # Clear any previous input
        search_box.send_keys(term + Keys.ENTER)  # Enter search term and press Enter

        # Wait for search results to load
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'issue-list')))

        # Check the status of issues
        issues = driver.find_elements(By.CLASS_NAME, 'issue-status')  # Replace with actual class name for issue statuses
        for issue in issues:
            status = issue.text
            print(f"Issue for '{term}': Status - {status}")

# Function to search for a specific ticket by its ID
def search_ticket(driver, ticket_id):
    search_box = driver.find_element(By.ID, 'quickSearchInput')  # Replace with actual ID of the search box
    search_box.clear()
    search_box.send_keys(ticket_id + Keys.ENTER)  # Enter the ticket ID and press Enter

    # Wait for the ticket page to load
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'summary-val')))  # Replace with actual ID or class name of an element on the ticket page

    # Extract and display the status of the ticket
    status = driver.find_element(By.ID, 'status-val').text  # Replace with actual ID or class name for the status field
    print(f"Ticket {ticket_id} Status: {status}")

# Function to initiate the search process
def start_search():
    # Get the search terms from the user input
    search_terms = entry.get().split(',')

    # Set up WebDriver
    driver = webdriver.Chrome()

    try:
        # Open Jira login page
        driver.get('https://jira.cpg.dell.com/login.jsp')
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1erlht4')))

        # Log in
        element = driver.find_element(By.CLASS_NAME, 'css-1erlht4')
        element.click()
        username_field = driver.find_element(By.ID, "login-form-username")
        username_field.send_keys("Kirana_MS")

        password_field = driver.find_element(By.ID, "login-form-password")
        password_field.send_keys("Kiran@1808")

        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

        # Wait until the dashboard loads
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'dashboard')))

        # Perform searches
        search_jira(driver, search_terms)

        # Prompt to search for a specific ticket
        ticket_id = simpledialog.askstring("Input", "Enter the ticket ID to search:", parent=root)
        if ticket_id:
            search_ticket(driver, ticket_id)

    finally:
        # Close the browser
        driver.quit()

# Set up the GUI
root = tk.Tk()
root.title("Jira Issue Search")

# Label and entry field
label = tk.Label(root, text="Enter search terms (comma-separated):")
label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Search button
search_button = tk.Button(root, text="Search Jira", command=start_search)
search_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
