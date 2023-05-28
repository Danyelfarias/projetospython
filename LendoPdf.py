import PyPDF2
# converter o arquivo em forma para a forma de binario
Convertido_binario = open('C:\\Users\\engen\\Documents\\2. Danyel\\Livro de Poemas UFSJ.pdf', 'rb')

# ler aquivo pdf com a funçao da biblioteca,
# . obs so aceita ser lido se tiver em forma de binario
DadosPDF= PyPDF2.PdfReader(Convertido_binario)
print(str(DadosPDF.numPages))
