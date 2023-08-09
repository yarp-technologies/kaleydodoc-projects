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
        subprocess.run(["docker",
                        "exec",
                        "libreoffice",
                        "libreoffice",
                        "--convert-to", "pdf",
                        "--outdir",
                         FILE_FOLDER,
                         self.file])
        delete_path = FILE_FOLDER + '/' + self.file.split('/')[-1]
        os.remove(delete_path)
        path = FILE_FOLDER + '/' + self.file.split('/')[-1].split('.')[0] + '.pdf'
        return path
