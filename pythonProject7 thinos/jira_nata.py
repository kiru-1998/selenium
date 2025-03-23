from jira import JIRA

# JIRA credentials
JIRA_URL = 'https://your-jira-instance.atlassian.net'  # Replace with your JIRA instance URL
JIRA_USERNAME = 'your-email@example.com'  # Replace with your JIRA email or username
JIRA_API_TOKEN = 'your-api-token'  # Replace with your JIRA API token
ISSUE_KEY = 'PROJECT-123'  # Replace with your issue key
FILE_PATH = '/path/to/your/logfile.log'  # Replace with the path to your local log file

def attach_file_to_jira_issue(jira_url, username, api_token, issue_key, file_path):
    try:
        # Connect to JIRA
        jira = JIRA(server=jira_url, basic_auth=(username, api_token))

        # Attach the file to the issue
        with open(file_path, 'rb') as file:
            jira.add_attachment(issue=issue_key, attachment=file)
        print(f"File {file_path} attached to issue {issue_key} successfully.")

    except Exception as e:

        print(f"An error occurred while attaching the file: {e}")

# Call the function
attach_file_to_jira_issue(JIRA_URL, JIRA_USERNAME, JIRA_API_TOKEN, ISSUE_KEY, FILE_PATH)
