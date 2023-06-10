import random

pc = [1, 2, 3, 4, 5]
pc_escolhido = random.choice(pc)

play = int(input("Digite um número entre 1 e 5: "))

if play == pc_escolhido:
    print("Você acertou o número que o PC pensou!")
else:
    print("Você errou.")
    print(f"O PC pensou no número {pc_escolhido}.")
