# Find and fill in the username and password fields
try:

    # Navigate to the JIRA login page
    driver.get('https://jira.cpg.dell.com/login.jsp')



        driver.find_element(By.ID, 'login-form-username').send_keys(username)
        driver.find_element(By.ID, 'login-form-password').send_keys(password)
        driver.find_element(By.ID, 'login-form-password').send_keys(Keys.RETURN)

        # Wait for the login process to complete
        time.sleep(5)  # Adjust the sleep time as necessary

        # Navigate to the Create Issue page
        driver.find_element(By.ID, 'create_link').click()

        # Wait for the Create Issue modal to open
        time.sleep(3)  # Adjust the sleep time as necessary

        # Fill in the project field
        project_field = driver.find_element(By.ID, 'project-field')
        project_field.clear()
        project_field.send_keys(project_key)
        project_field.send_keys(Keys.TAB)

        # Fill in the issue type field
        issue_type_field = driver.find_element(By.ID, 'issuetype-field')
        issue_type_field.clear()
        issue_type_field.send_keys(issue_type)
        issue_type_field.send_keys(Keys.TAB)

        # Fill in the summary field
        summary_field = driver.find_element(By.ID, 'summary')
        summary_field.send_keys(summary)

        # Fill in the description field
        description_field = driver.find_element(By.ID, 'description')
        description_field.send_keys(description)

        # Submit the form
        driver.find_element(By.ID, 'create-issue-submit').click()

        # Wait for the issue to be created
        time.sleep(5)  # Adjust the sleep time as necessary

        print("Issue created successfully.")

    finally:
        # Close the browser
        driver.quit()

# Example usage
jira_url = 'https://your-jira-instance.atlassian.net'
username = 'your-username'
password = 'your-password'
project_key = 'PROJECT'
summary = 'Issue created by Python Selenium script'
description = 'This issue was created automatically using Selenium'
issue_type = 'Task'

create_jira_issue_selenium(jira_url, username, password, project_key, summary, description, issue_type)
