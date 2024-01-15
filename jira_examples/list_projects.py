import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://saikishorereddy.atlassian.net/rest/api/3/project"

API_TOKEN = " "
auth = HTTPBasicAuth("rachumallasaikishore@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.get(
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=2))


output = json.loads(response.text)

name = output[2]["name"]

print("projectName:", name)