import requests
import json

file = {'file': open("IT-Test-template.docx", 'rb')}

regex = {"Browser": "Gooogle",
         "Version": "0.0.0.0.1",
         "IP": "0.0.0.127",
         "Location": "Russia",
         "Created": "Konstantine"}

data = {"tags": json.dumps(regex)}

res = requests.post("http://0.0.0.0:7777/api_module", files=file, data=data)

with open("out_files/out.pdf", "wb") as code:
    code.write(res.content)
