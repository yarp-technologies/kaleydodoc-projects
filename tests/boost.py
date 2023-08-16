import unittest
import requests
import json
import time

class TestPDFPlaceholder(unittest.TestCase):

    def test_mid_stat_file(self):
        file = {'file': open("./test_files/typical.docx", 'rb')}
        tags = {"Browser": "Gooogle",
                "Version": "0.0.0.0.1",
                "IP": "0.0.0.127",
                "Location": "Russia",
                "Created": "Konstantine"}
        data = {"tags": json.dumps(tags)}
        start = time.time()
        res = requests.post("http://81.200.156.178:7777/api_module", files=file, data=data)
        end = time.time() - start
        print("Test mid stat file: " + str(end))
        self.assertEqual(res.status_code, 200)