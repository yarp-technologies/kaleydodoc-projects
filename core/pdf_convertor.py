import subprocess
import os
import requests
from constants.variables import *
from constants.msg import ErrorType


class Convert2PDF:

    def __init__(self, file_path: str):
        # Todo под расширение для других форматов
        self.file = file_path
        self.error = ErrorType.ok

    def DocxToPdf(self):
        # Определите URL и порт LibreOffice Online сервиса
        libreoffice_online_url = "http://soffice:9980"  # Имя сервиса из вашего docker-compose.yml

        # Отправьте запрос на конвертацию
        response = requests.post(
            f"{libreoffice_online_url}/lool/convert-to/pdf",
            data=open(self.file, "rb").read(),
            headers={"content-type": "application/octet-stream"}
        )

        if response.status_code == 200:
            pdf_path = os.path.join(FILE_FOLDER, f"{os.path.basename(self.file).split('.')[0]}.pdf")
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(response.content)

            delete_path = os.path.join(FILE_FOLDER, os.path.basename(self.file))
            os.remove(delete_path)

            return pdf_path
        else:
            print(f"Ошибка при конвертации: {response.status_code}")
            return None

'''
    def DocxToPdf(self):
        subprocess.call(['soffice',
                         '--headless',
                         '--convert-to',
                         'pdf',
                         '--outdir',
                         FILE_FOLDER,
                         self.file])
        delete_path = FILE_FOLDER + '/' + self.file.split('/')[-1]
        os.remove(delete_path)
        path = FILE_FOLDER + '/' + self.file.split('/')[-1].split('.')[0] + '.pdf'
        return path
'''


