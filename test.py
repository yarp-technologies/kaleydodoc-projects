import requests

url = "http://0.0.0.0:7777/api/access_token"
username = "murder"
password = "12345"
data = {
        "username": username,
        "password": password
    }
res = requests.post(f'{url}', data=data)
data = res.json()
print(res.status_code)


url = "http://0.0.0.0:7777/api_user/placeholder_items"
headers = {"Authorization": f"{data['token_type']} {data['access_token']}"}
files = {"file": open("test_files/typical_random_style.docx", "rb")}
res = requests.post(url, files=files, headers=headers)
tags = res.json()

print(res.status_code)

url = "http://0.0.0.0:7777/api/access_token"
username = "murder"
password = "12345"
data = {
        "username": username,
        "password": password
    }
res = requests.post(f'{url}', data=data)
data = res.json()
print(res.status_code)

tags['filename'] = "typical_random_style.docx"
headers = {
    "Authorization": f"{data['token_type']} {data['access_token']}",
    'Content-Type': 'application/json'
}

url = "http://0.0.0.0:7777/api_user/placeholder_process"
res = requests.post(url, data={"data": tags}, headers=headers)
print(res.status_code)

