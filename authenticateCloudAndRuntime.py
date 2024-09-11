import json, requests

url = "https://api0.prismacloud.io/login"
username = "3d852ead-cf40-4424-b9f3-5ed3a76e74ae" #Access Key ID
password = "Hkb9dM2qj0bqaa2abaMYyyQDVj0=" #Secret Key

payload = json.dumps({
    "username": f"{username}",
    "password": f"{password}",
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
data = response.json()
if(data['token']):
    print("Successfully generated token from Cloud Module")
    global generatedCloudToken 
    generatedCloudToken = data['token']
else:
    print("Error:\n" + response.text)
if('generatedCloudToken' in globals()):
    url = "https://app0.cloud.twistlock.com/panw-app0-310/api/v1/authenticate"

    payload = json.dumps({
        "username": f"{username}",
        "password": f"{password}",
        "token": generatedCloudToken,
        })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
else:
    print("Cloud Token Not Generated")
