import requests
import json


# регистрация через апи
url = "http://81.200.156.178:7777/api/signup"
data = {
    "name": "Nik",
    "username": "redrum",
    "email": "12345",
    "password": "nik@mail.ru"
}
res = requests.post(url, data=data)
print(res.json())

# получение access_token
url = "http://81.200.156.178:7777/api/access_token"
username = "murder"
password = "12345"
data = {
        "username": username,
        "password": password
    }
res = requests.post(f'{url}', data=data)
token = res.json()


# получение тэгов на заполнение (не обязательно)
url = "http://81.200.156.178:7777/api_user/placeholder_items"
headers = {"Authorization": f"{token['token_type']} {token['access_token']}"}
files = {"file": open("test_files/typical_random_style.docx", "rb")}
res = requests.post(url, files=files, headers=headers)
data = res.json()
data['filename'] = "typical_random_style.docx"


# заполнение и коныертация
url = "http://81.200.156.178:7777/api_user/placeholder_process"
res = requests.post(url, json=data, headers=headers)
with open('out_test_files/out.pdf', 'wb') as file:
    file.write(res.content)
print(res.status_code)


