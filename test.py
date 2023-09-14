import requests
import json

# Todo: выгрузка бинарника
# Todo: выгрузка ссылка


# регистрация через апи
url = "http://81.200.156.178:7777/api/signup"
data = {
    "name": "Nik",
    "username": "redrum",
    "email": "nik@mail.ru",
    "password": "12345"
}
res = requests.post(url, data=data)
print(res.json())

# получение access_token
url = "http://81.200.156.178:7777/api/access_token"
username = "redrum"
password = "12345"
data = {
        "username": username,
        "password": password
    }
res = requests.post(f'{url}', data=data)
token = res.json()
print(token)


# получение тэгов на заполнение (не обязательно)
url = "http://81.200.156.178:7777/api_user/placeholder_items"
headers = {"Authorization": f"{token['token_type']} {token['access_token']}"}
files = {"file": open("test_files/typical_random_style.docx", "rb")}
res = requests.post(url, files=files, headers=headers)
data = res.json()
print(data)
data['filename'] = "typical_random_style.docx"
data["Browser"] = "Gooogle"
data["Version"] = "0.0.0.0.1"
data["IP"] = "0.0.0.127"
data["Location"] = "Russia"
data["Created"] = "Konstantine"


# заполнение и конвертация
url = "http://81.200.156.178:7777/api_user/placeholder_process"
res = requests.post(url, json=data, headers=headers)

with open('out_test_files/out.pdf', 'wb') as file:
    file.write(res.content)
print(res.status_code)

