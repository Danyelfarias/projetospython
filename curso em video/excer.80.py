
lista=[]
while True:
    
    print('adicione um valor a lista')
    valores= input('qual valor: ')
    if valores.lower()=='sair':
        break
    
    else:   
        lista.append(valores)
        lista.sort()
        print(lista)
        posiçao=lista.index(valores)
        print(f'ESSE VALOR ESTA NA PODIÇAO: {posiçao+1}')
    
    
        
print('encerrado')
print(lista)