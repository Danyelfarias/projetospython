n1 = int(input('escolha um número: '))
n2 = int(input('escolha outro número: '))
print('1-somar 2-multiplicar 3-maior 4-escolher novos números 5-fechar programa')
escolha = int(input('escolha seu número: '))

while escolha != 5:
    if escolha == 1:
        soma = n1 + n2
        print(f'a soma desses números é {soma}')
    elif escolha == 2:
        multiplicacao = n1 * n2
        print(f'o resultado da multiplicação desses números é {multiplicacao}')
    elif escolha == 3:
        if n1 > n2:
            print(f'o maior número entre os dois é {n1}')
        else:
            print(f'o maior número entre os dois é {n2}')
    elif escolha == 4:
        n1 = int(input('escolha um número: '))
        n2 = int(input('escolha outro número: '))
        print('e agora o que vc deseja fazer com esses números: ')
        print('1-somar 2-multiplicar 3-maior 4-escolher novos números 5-fechar programa')
    escolha = int(input('escolha seu número: '))

print('programa finalizado')
