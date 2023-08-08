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
        url = "http://localhost:3000/unoconv/pdf"
        files = {"file": open(self.file, "rb")}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            pdf_path = os.path.join(FILE_FOLDER, os.path.basename(self.file).split('.')[0] + ".pdf")
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(response.content)

        '''subprocess.call(['soffice',
                         '--headless',
                         '--convert-to',
                         'pdf',
                         '--outdir',
                         FILE_FOLDER,
                         self.file])
        '''
        delete_path = FILE_FOLDER + '/' + self.file.split('/')[-1]
        os.remove(delete_path)
        path = FILE_FOLDER + '/' + self.file.split('/')[-1].split('.')[0] + '.pdf'
        return path
