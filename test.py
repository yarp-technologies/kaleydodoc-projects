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
        libreoffice_container = client.containers.get("pdf_placeholder-libreoffice-1")
        cmd = f"libreoffice --headless --convert-to pdf --outdir files test_files/{self.file}"
        result = libreoffice_container.exec_run(cmd)
        delete_path = self.file
        # os.remove(delete_path)
        pdf_path = f"/files/{os.path.basename(self.file).split('.')[0]}.pdf"
        return pdf_path

print(Convert2PDF("typical_random_style.docx").DocxToPdf())