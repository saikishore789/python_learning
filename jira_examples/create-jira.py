import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://saikishorereddy.atlassian.net/rest/api/3/issue"

API_TOKEN="ATATT3xFfGF0SkdzrnMml6gEeFo0fDXF6lngH2MyjwCTEQTCwkXavDw4fSSY-HhR6tIXVpc9zW3LK5kY8XsipSMB82AzgWo-oqcWGmxwZjaQ412Z_Ix4crzhxyip5l6A37ro2_5sEW5ZyaeZqojw4wA4VKpHtmlr6zLN0FUhIg5o-NXJbqZZpak=6010CC80"

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