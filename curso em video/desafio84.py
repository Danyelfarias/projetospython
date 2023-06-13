lista=list()
dados=[]
while True:
    nome=str(input('nome: '))
    peso=int(input('peso: '))
    lista.append(nome)
    lista.append(peso)
    if len(dados)==0:
        mai=men=lista[1]
        if lista[1]>mai:
            mai=lista[1]
        if lista[1]<men:
            lista[1]=men
    dados.append(lista[:])#tirar um a copia da lista 
    lista=[]
    pergunta=str(input('deseja continuar'))
    if pergunta.upper() in 'N':
        break
print(f'ao todo vc cadastrou {len(dados)} pessoas')
print(f'o maior peso é {mai}')
print(f'o menor peso é {men}')
for p in lista:
    if p[1]==mai:
        print(p[0])
#codigo feito pelo chat gpt
# dados = []
# mai = float('-inf')  # valor inicial para o maior peso
# men = float('inf')  # valor inicial para o menor peso

# while True:
#     nome = input('nome: ')
#     peso = int(input('peso: '))

#     if peso > mai:
#         mai = peso
#     if peso < men:
#         men = peso

#     lista = [nome, peso]
#     dados.append(lista[:])
    
#     pergunta = input('deseja continuar? ')
#     if pergunta.upper() == 'N':
#         break

# print(f'ao todo, você cadastrou {len(dados)} pessoas')
# print(f'o maior peso é {mai}')
# print(f'o menor peso é {men}')

# for pessoa in dados:
#     if pessoa[1] == mai:
#         print(pessoa[0])
