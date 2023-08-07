import subprocess
import os
from constants.variables import *


class Convert2PDF:

    def __init__(self, file_path: str):
        # Todo под расширение для других форматов
        self.file = file_path

    def DocxToPdf(self):
        try:
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
        except:
            return None
