from docx import Document
from weasyprint import HTML

def convert_docx_to_pdf(docx_path, pdf_path):
    try:
        # Чтение содержимого .docx файла
        doc = Document(docx_path)
        paragraphs = []
        for para in doc.paragraphs:
            paragraphs.append(para.text)

        # Сохранение содержимого во временный HTML файл
        html_content = "<br>".join(paragraphs)
        html_temp_file = "/tmp/temp.html"
        with open(html_temp_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        # Генерация PDF из HTML и сохранение его по указанному пути
        HTML(string=html_content).write_pdf(pdf_path)

        print(f"Конвертация завершена. Результат сохранен в: {pdf_path}")
    except Exception as e:
        print(f"Произошла ошибка при конвертации: {e}")

if __name__ == "__main__":
    docx_file_path = "test_files/typical.docx"
    pdf_file_path = "output.pdf"
    convert_docx_to_pdf(docx_file_path, pdf_file_path)