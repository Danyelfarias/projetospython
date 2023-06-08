soma = 0

while True:
    produto = input('QUAL PRODUTO VOCÊ QUER COMPRAR (ou digite "sair" para encerrar): ')

    if produto == 'sair':
        break

    while True:
        try:
            preco = float(input('Qual o preço do produto? R$ '))
            break
        except ValueError:
            print('Por favor, insira um valor numérico válido.')

    soma += preco

    print('1 - Continuar a compra')
    print('2 - Encerrar a compra')
    confirmacao = int(input('Escolha uma opção: '))

    if confirmacao == 2:
        break

print('Valor total da compra: R$', soma)
print('Compra encerrada')
