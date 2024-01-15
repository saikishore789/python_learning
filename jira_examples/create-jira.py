import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://saikishorereddy.atlassian.net/rest/api/3/issue"

API_TOKEN="ATATT3xFfGF0cNhLHOHhMdKg4XIrrTsIY7TrUrsG0FEV6iKqfW3RsVzeQhwfCYNZJ9_j9VnXQuCG__HUpkMWU-ArUF8snnBZtpC8XcblERxHr2l6Irwu6M8nWtXdzm9oVTIHwHvQK17VTV0e0Qu-Q0rOGMHZSh0brobmrM6pg3CeMUVpfpt_BA4=8F34E289"

auth = HTTPBasicAuth("rachumallasaikishore@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "SAI"
    },
    "issuetype": {
      "id": "10006"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))