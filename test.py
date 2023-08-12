import sys
import os
import comtypes.client

wdFormatPDF = 17

in_file = os.path.abspath("test_files/typical.docx")
out_file = os.path.abspath("out.pdf")

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()