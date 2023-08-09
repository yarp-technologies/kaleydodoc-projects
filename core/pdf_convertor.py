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
        '''
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
        :return:
        '''
        client = docker.from_env()
        libreoffice_container = client.containers.get("pdf_placeholder-libreoffice-1")
        cmd = f'soffice ' \
              f'--headless ' \
              f'--convert-to pdf:writer_pdf_Export ' \
              f'--outdir ' \
              '"-env:UserInstallation=file:///tmp/LibreOffice_Conversion_${USER}"' \
              f'{FILE_FOLDER} ' \
              f'{self.file}'
        result = libreoffice_container.exec_run(cmd)
        delete_path = FILE_FOLDER + '/' + self.file.split('/')[-1]
        os.remove(delete_path)
        pdf_path = FILE_FOLDER + '/' + self.file.split('/')[-1].split('.')[0] + '.pdf'
        return pdf_path
