import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://saikishorereddy.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0Ox-A7i5-d1oyxe5_Vszp9LdQA4LGHH5V-NtCtwPbqdeB1OZNRE6ETqkQLVJOY54fMEzxHlQH1oMLZzN2Wx0i2416ko-PsWO-sWGKx9FdPxf7SUGBsc7Z0BcoG_jzPi5RUmVPpw_VbSa0kKvyl5PpT7rh0RMnsQBR73RTvUAVcUw=06EE974F"

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