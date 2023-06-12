lista=[]
parlista=[]
inparlista=[]
while True:
    valor= int(input('qual valor vc quer inserir a lista: '))
    lista.append(int(valor))
    escolha= input('quer continuar: ')
    if escolha.upper() =='N':
        break
print(lista)

for termos in lista:
    if termos%2==0:
        parlista.append(termos)
        print(parlista)
    else:
        inparlista.append(termos)
        print(inparlista)
