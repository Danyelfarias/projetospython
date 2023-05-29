import win32com.client
from datetime import datetime, timedelta
import os

data_de_ontem = datetime.now().date() - timedelta(days=1)

outlook = win32com.client.Dispatch('Outlook.Application')
email = outlook.CreateItem(0)
email.To = 'danyelzimfarias@gmail.com'
email.Subject = f'DT´s referente ao dia {data_de_ontem}'
email.HTMLBody = f'Documento de transporte referente ao dia {data_de_ontem}'

nome_do_arquivo =input('Nome do arquivo em PDF (não esqueça de incluir a extensão do arquivo): ')
caminho_do_arquivo = os.path.expanduser(fr"C:\Users\engen\Desktop\{nome_do_arquivo}")

if os.path.exists(caminho_do_arquivo):
    email.Attachments.Add(caminho_do_arquivo)
    email.Send()
    print('Email enviado.')
else:
    print(f'O arquivo {caminho_do_arquivo} não foi encontrado.')

