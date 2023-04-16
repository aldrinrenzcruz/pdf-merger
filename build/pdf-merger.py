import PyPDF2
import os

def merge_pdfs():
    folder_path = os.getcwd()
    files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
    files.sort()
    merged_pdf = PyPDF2.PdfWriter()
    for file in files:
        with open(os.path.join(folder_path, file), 'rb') as pdf_file:
            pdf = PyPDF2.PdfReader(pdf_file)
            for page in pdf.pages:
                merged_pdf.add_page(page)
    with open("merged.pdf", 'wb') as out_file:
        merged_pdf.write(out_file)

merge_pdfs()
