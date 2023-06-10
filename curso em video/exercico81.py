lista=[]
cont=0
while True:
    termos= input('ensira um valor: ')
    if termos.upper() =='N':
        break
    else:
        lista.append(termos)
        lista.sort(reverse=True)
        cont+=1
print('encerrado')
if '5' in lista:
    print(f'sim , a lista {lista}  tem o termo 5')
    print(f'vc digitou {cont} número na lista')
else:
    print('nao tem o termo 5')
    print(f'vc digitou {cont} número na lista')

