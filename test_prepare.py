import requests
import json

file = {'file': open("./test_files/typical.docx", 'rb')}

regex = {"Browser": "Gooogle",
         "Version": "0.0.0.0.1",
         "IP": "0.0.0.127",
         "Location": "Russia",
         "Created": "Konstantine"}

data = {"tags": json.dumps(regex)}

res = requests.post("http://81.200.156.178:7777/api_module", files=file, data=data)

print(res.text)

with open("out_files/out.pdf", "wb") as code:
    code.write(res.content)
