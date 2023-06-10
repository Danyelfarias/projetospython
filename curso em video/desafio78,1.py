lista=[]
while True:
    valores=0
    valores= input('digite o valor')
    if valores.lower()=="sair":
        break
    lista.append(int(valores))
print(f'o menor num é: {min(lista)}')
print(f'o maior num é: {max(lista)}')
        
    

    