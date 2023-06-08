
print(F'CADASTRO DE UMA PESSOA')
print(F'-------------------------------')
cont=0
while True:
    nome=str(input('nome:'))
    idade=int(input('idade:'))
    if idade>18:
        cont+=1
    print(F'-------------------------------')
    opcao=str(input('DESEJA CADASTRA MAIS ALGUÉM?/SIM/NAO ')).upper().strip()

    if opcao=='NAO':
        break
print('PROGRAMA DE CADASTRO ENCERRADO!!!')
print(f'foram cadastradas {cont} maiores de idade')

