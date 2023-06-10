# lista=[]

# while True:

#     adicinar= input('quer adicionar algum valor SIM OU NAO: ')
#     if adicinar.upper() == 'S':
#         if adicinar not in lista:
#             adicinar=int(input('digite um valor: '))
#             lista.append(adicinar)
#             print('adicinado com sucesso')
#         else:
#             print('por favor adicionar um outro numero que nao tenha na lista!!!!')

#     elif adicinar.upper() == 'N':
#         break
#     # else:
#     #     adicinar=adicinar1
# print(f"voce adicioneou os número {lista}")
# lista = []

# while True:
#     adicionar = input('Quer adicionar algum valor? (SIM ou NAO): ')
    
#     if adicionar.upper() == 'SIM':
#         valor = int(input('Digite um valor: '))
        
#         if valor in lista:
#             print('O número já está na lista. Por favor, adicione um número diferente!')
#         else:
#             lista.append(valor)
#             print('Adicionado com sucesso!')

#     elif adicionar.upper() == 'NAO':
#         break

# print(f"Você adicionou os números: {lista}")
lista = []

while True:
    adicionar = input('Quer adicionar algum valor? (SIM ou NAO): ')
    
    if adicionar.upper() == 'SIM':
        valor = int(input('Digite um valor: '))
        
        if valor not in lista:
            lista.append(valor)
            print('Adicionado com sucesso!')
        else:
            print('Por favor, adicione um número que não esteja na lista!')
    
    elif adicionar.upper() == 'NAO':
        break

print(f"Você adicionou os números: {lista}")
