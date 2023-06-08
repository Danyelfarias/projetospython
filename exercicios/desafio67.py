import random

cont = 0

while True:
    escolhasPC = ['P', 'I']
    escolha = input('Par ou ímpar? ').strip().upper()
    pc = random.choice(escolhasPC).upper()
    cont += 1

    if escolha == pc:
        break

print(f'Você acertou! Parabéns! Você acertou na tentativa {cont}.')
