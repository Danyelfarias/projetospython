from pypdf import PdfFileReader

def ler_parte_pdf(arquivo_pdf, pagina_inicial, pagina_final):
    texto = ""
    with open(arquivo_pdf, "rb") as arquivo:
        leitor_pdf = PdfFileReader(arquivo)
        for pagina_num in range(pagina_inicial - 1, pagina_final):
            pagina = leitor_pdf.getPage(pagina_num)
            texto += pagina.extractText()
    return texto

arquivo_pdf = r'C:\Users\FARIAS\Documents\3. Danyel\projetospython\DT Farma CE 25.05.2023 (1).pdf'
pagina_inicial = 1
pagina_final = 3

texto_extraido = ler_parte_pdf(arquivo_pdf, pagina_inicial, pagina_final)

print(texto_extraido)

