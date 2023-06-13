matriz = [[[], [], [], []],
          [[], [], [], []]]
cont=0
# matriz[0].append(teste)
for linha in range(2):
    for coluna in range(4):
        num=int(input('coloque os numero dessa matriz: '))
        matriz[linha][coluna].append(num)
        cont+=1

for linha in matriz:
    for elemento in linha :
        print(f"[{elemento[0]:^5}]", end=' ')
    print()
