import subprocess
import os
from constants.variables import *
from constants.msg import ErrorType
import docker


class Convert2PDF:

    def __init__(self, file_path: str):
        # Todo под расширение для других форматов
        self.file = file_path
        self.error = ErrorType.ok

    def DocxToPdf(self):
        client = docker.from_env()
        print(1)
        libreoffice_container = client.containers.get("pdf_placeholder-libreoffice-1")
        print(2)
        cmd = f"libreoffice --headless --convert-to pdf --outdir {FILE_FOLDER} {self.file}"
        print(3)
        result = libreoffice_container.exec_run(cmd)
        print(4)
        delete_path = FILE_FOLDER + '/' + self.file.split('/')[-1]
        os.remove(delete_path)
        pdf_path = f"/files/{os.path.splitext(self.file)[0]}.pdf"
        return pdf_path

print(Convert2PDF("test_files/typical_random_style.docx").DocxToPdf())