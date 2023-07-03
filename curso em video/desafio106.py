def ajuda(a):
    help(a)

while True:
    escolha=input('digite a funçao: ')
    if escolha in 'Nn':
        break
    
    ajuda(escolha)