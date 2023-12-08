import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://saikishorereddy.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0SkdzrnMml6gEeFo0fDXF6lngH2MyjwCTEQTCwkXavDw4fSSY-HhR6tIXVpc9zW3LK5kY8XsipSMB82AzgWo-oqcWGmxwZjaQ412Z_Ix4crzhxyip5l6A37ro2_5sEW5ZyaeZqojw4wA4VKpHtmlr6zLN0FUhIg5o-NXJbqZZpak=6010CC80"

auth = HTTPBasicAuth("rachumallasaikishore@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=2))


output = json.loads(response.text)

name = output[2]["name"]

print("projectName:", name)