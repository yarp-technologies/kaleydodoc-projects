from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_docx_to_pdf(docx_file_path, pdf_file_path):
    # Открываем DOCX файл
    doc = Document(docx_file_path)

    # Создаем PDF файл с помощью reportlab
    c = canvas.Canvas(pdf_file_path, pagesize=letter)

    for para in doc.paragraphs:
        c.drawString(100, 700, para.text)
        c.showPage()

    c.save()


# Укажите пути к вашим файлам
docx_path = "test_files/typical.docx"
pdf_path = "output.pdf"

convert_docx_to_pdf(docx_path, pdf_path)