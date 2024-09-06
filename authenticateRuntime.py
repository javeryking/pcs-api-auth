import requests
import json

url = "https://app0.cloud.twistlock.com/panw-app0-310/api/v1/authenticate"
username = ""
password = ""
token = ""

payload = json.dumps({
    "username": f"{username}",
    "password": f"{password}",
    "token" : f"{token}"
    })
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
