import requests

url = 'https://httpbin.org/get'

headers = {'Content-Type': 'text/html'}

response = requests.get(url, headers=headers)

print(response)


response1 = requests.get('https://httpbin.org/get')
print(response1.headers)