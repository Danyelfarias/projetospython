matriz = [[[], [], [], []],
          [[], [], [], []]]

cont = 0

for linha in range(2):
    for coluna in range(4):
        num = int(input('Digite um número: '))
        matriz[linha][coluna].append(num)
        cont += 1

for linha in matriz:
    for elemento in linha:
        print(*elemento, end=' ')
    print()
