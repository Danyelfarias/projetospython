import PySimpleGUI as sg
layout = [
  [sg.Text('nome do arquivo')],
  [sg.InputText()],
  [sg.Button('buscar'),sg.Button('cancelar')],
  [sg.Text('texto do confimação')]]

janela = sg.Window('emviador de arquivo',layout)
while True: 
    evento,valores = janela.read()
    if evento==sg.WIN_CLOSED or evento=='cancelar':
        break
