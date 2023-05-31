import PyPDF2

# Abrir o arquivo PDF em modo binário
arquivo_pdf = open('C:\\Users\\engen\\Documents\\2. Danyel\\DT Farma CE 25.05.2023.pdf', 'rb')

# Criar um objeto PdfReader
dados_pdf = PyPDF2.PdfReader(arquivo_pdf)

# Obter o número de páginas
num_paginas = len(dados_pdf.pages)
print(num_paginas)

# Obter a página 1
numero_pag =int(input('escolha o número da página: '))
# assim a página vai fica mais dinamica
pagina = dados_pdf.pages[numero_pag - 1]

# Extrair o texto da página 1
extrair_pagina1 = pagina1.extract_text()
print(extrair_pagina1)

# Fechar o arquivo PDF
arquivo_pdf.close()
