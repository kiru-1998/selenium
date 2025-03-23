import requests
from requests.auth import HTTPBasicAuth
import json

# Replace with your Jira instance URL, username, and password
jira_url = "https://jira.cpg.dell.com/rest/api/2/"
username = "Kirana_MS"
password = "Kiran@1808"

# Authentication
auth = HTTPBasicAuth(username, password)


jql_query = 'project = "Dell ThinOS" AND "Bug Source" = Customer'

# API URL for searching issuesa
search_url = jira_url + "search"

# Parameters for the search API
params = {
    'jql': jql_query,
    'maxResults': 100,  # Adjust as needed
    'fields': ['summary', 'status', 'assignee']  # Adjust fields as needed
}

# Send the request to Jira
response = requests.get(search_url, auth=auth, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    issues = response.json()

    # Print out details for each issue
    print(f"Found {len(issues['issues'])} issue(s) related to 'Customer':\n")
    for issue in issues['issues']:
        print(f"Summary: {issue['fields']['summary']}")
        print(f"Status: {issue['fields']['status']['name']}")
        print(
            f"Assignee: {issue['fields']['assignee']['displayName'] if issue['fields']['assignee'] else 'Unassigned'}")
        print('-' * 40)
else:
    print(f"Failed to retrieve issues: {response.status_code} - {response.text}")
