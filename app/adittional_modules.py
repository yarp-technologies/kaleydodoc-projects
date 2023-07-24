import shutil
import os
import uuid
from constants.variables import *
from fastapi import UploadFile, File


def save_file(input_file_data: UploadFile = File(None)):
    filename = str(uuid.uuid4())[:8] + '_' + input_file_data.filename
    path = os.path.join(FILE_FOLDER, filename)
    with open(f'{path}', "wb") as buffer:
        shutil.copyfileobj(input_file_data.file, buffer)
    return path

def prepare_regex(text: str):
    reg = text.split("\r\n")
    regex = {}
    for tag in reg:
        value = tag.split(":")
        regex[value[0]] = value[1]
    return regex