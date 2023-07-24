from core.core_object import Core
from pathlib import Path

regex = {r"<<Browser>>": "Gooogle",
         "<<Version>>": "0.0.0.0.1",
         "<<IP>>": "0.0.0.127",
         "<<Location>>": "Russia",
         "<<Created>>": "Konstantine"}

filler = Core("IT-Test-template.docx", regex).process()

print(Path(filler).name)
print(filler)