import requests
import json

url = "https://api0.prismacloud.io/login"

payload = json.dumps({
    "username": "",
    "password": "",
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
