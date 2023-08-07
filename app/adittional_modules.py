import shutil
import os
import uuid
from constants.variables import *
from fastapi import UploadFile, File


def save_file(input_file_data: UploadFile = File(None)):
    try:
        filename = str(uuid.uuid4())[:8] + '_' + input_file_data.filename
        path = os.path.join(FILE_FOLDER, filename)
        with open(f'{path}', "wb") as buffer:
            shutil.copyfileobj(input_file_data.file, buffer)
        return path
    except:
        return None

def prepare_regex(text):
    regex = {}
    if text is None:
        return regex
    reg = text.split("\r\n")
    for tag in reg:
        if tag.find(":") != -1:
            value = tag.replace(" ", "").split(":")
            regex[value[0]] = value[1]
    return regex