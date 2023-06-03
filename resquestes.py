import requests

# Defina a URL do site de conversão de PDF
url = 'https://www.pdf2go.com/pt/tornar-pdf-pesquisavel'

# Defina o caminho do arquivo PDF que você deseja converter
caminho_arquivo_pdf = 'C:\\Users\FARIAS\Downloads\example_nonsearchable.pdf'

# Envie a requisição POST com o arquivo PDF para o site
with open(caminho_arquivo_pdf, 'rb') as file:
    files = {'example_nonsearchable.pdf': file}
    response = requests.post(url, files=files)

# Verifique a resposta do site
if response.status_code == 200:
    # A resposta pode conter o PDF pesquisável ou um link para download
    # Você precisa analisar a estrutura do HTML para extrair a informação desejada
    # Usando BeautifulSoup ou outra biblioteca de parsing HTML

    # Exemplo de como extrair um link de download usando BeautifulSoup
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(response.content, 'html.parser')
    link_download = soup.find('a', {'class': 'link-download'})

    if link_download:
        # Obter o link de download
        download_url = link_download['href']

        # Baixar o PDF pesquisável
        response_download = requests.get(download_url)

        # Definir o caminho de destino para salvar o PDF pesquisável
        caminho_pdf_pesquisavel = '/caminho/para/o/arquivo_pesquisavel.pdf'

        # Salvar o PDF pesquisável no disco
        with open(caminho_pdf_pesquisavel, 'wb') as file:
            file.write(response_download.content)

        print('PDF pesquisável baixado com sucesso.')
    else:
        print('Não foi possível encontrar o link de download.')
else:
    print('A requisição não foi bem-sucedida.')
