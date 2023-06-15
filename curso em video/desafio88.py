import random

jogos = [list(range(0, 100)), list(range(0, 100)), list(range(0, 100)), list(range(0, 100)), list(range(0, 100)), list(range(0, 100))]
DADOS = []
cont = 0

for numerolance in range(6):
    for lances in range(10):
        aleatorio = random.choices(jogos[cont])
        DADOS.append(jogos[:])
        jogos.clear()
        cont += 1

print(DADOS)
