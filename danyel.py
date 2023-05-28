import PyPDF2

def ler_parte_pdf(arquivo_pdf, pagina_inicial, pagina_final):
    texto = ""
    with open(arquivo_pdf, "rb") as arquivo:
        leitor_pdf = PyPDF2.PdfFileReader(arquivo)
        for pagina_num in range(pagina_inicial - 1, pagina_final):
            pagina = leitor_pdf.getPage(pagina_num)
            texto += pagina.extractText()
    return texto

arquivo_pdf = 'DT Farma CE 25.05.2023 (1).pdf'
pagina_inicial = 1
pagina_final = 3

texto_extraido = ler_parte_pdf(arquivo_pdf, pagina_inicial, pagina_final)

print(texto_extraido)
