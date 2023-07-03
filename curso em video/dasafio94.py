cadastrados = []
Cad_mulher = []
quanti = 0
cont = 0
escolha = 'S'

while True:
    if escolha in 'Nn':
        break
    if escolha not in 'SNns':
        print('Resposta não identificada. Deseja continuar? [S/N]')
    
    cadastro = {'nome': '', 'sexo': '', 'idade': ''}
    
    nome = input('Nome: ')
    cadastro['nome'] = nome
    
    sexo = input('Sexo (F/M): ')
    if sexo not in 'FfMm':
        if sexo in 'fFMm':
            cadastro['sexo'] = sexo
        else:
            print('Escolha não reconhecida.')
            cadastro['sexo']= input('Sexo (F/M): ')
    
    idade = int(input('Idade: '))
    cadastro['idade'] = idade
    quanti += idade
    cont += 1
    cadastrados.append(cadastro)
    
    if sexo.upper() == 'F':
        Cad_mulher.append(cadastro)
    
    escolha = input('Deseja continuar cadastrando? (S/N): ')

media = quanti / cont

print(cadastrados)
print(f'Total de {len(cadastrados)} clientes cadastrados.')
print(f'A média das idades é {media}')
print(Cad_mulher)
print('-'*30)
print('==== Dados Cadastrados ====')
for i, n in enumerate(cadastrados):
    print(f'{"Nome:":<10} {n["nome"]:>20}')
    print(f'{"Idade:":<10} {n["idade"]:>20}')
    print(f'{"Sexo:":<10} {n["sexo"]:>20}')
    print('-' * 40)



    
    