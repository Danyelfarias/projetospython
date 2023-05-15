import os
import PyPDF2
caminho_do_arquivo="teste"
file_base_name=caminho_do_arquivo.replace('.pdf'," ")
output_folder_path=os.path.join(os.getcwd(),"output")

pdf = PyPDF2.PdfFileReader(caminho_do_arquivo)
for page_num in range(caminho_do_arquivo):
    PyPDF2.PdfFileWriter()
    PyPDF2.PdfWriter.addPage(pdf.getPage(page_num))