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
        try:
            client = docker.from_env()
            libreoffice_container = client.containers.get("pdf_placeholder-libreoffice-1")
            cmd = f'libreoffice ' \
                  f'--headless ' \
                  f'--convert-to pdf:writer_pdf_Export ' \
                  f'--outdir ' \
                  '"-env:UserInstallation=file:///tmp/LibreOffice_Conversion_${USER}" ' \
                  f'project/files ' \
                  f'{self.file}'
            result = libreoffice_container.exec_run(cmd)
            delete_path = FILE_FOLDER + '/' + self.file.split('/')[-1]
            os.remove(delete_path)
            pdf_path = FILE_FOLDER + '/' + self.file.split('/')[-1].split('.')[0] + '.pdf'
            return pdf_path
        except:
            return ErrorType.no_correct_doc
