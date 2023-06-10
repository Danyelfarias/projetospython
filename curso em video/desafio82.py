import random
numeros = tuple(range(1, 100))
ale1=random.choice(numeros)
ale2=random.choice(numeros)
ale3=random.choice(numeros)
ale4=random.choice(numeros)
maior=ale1
menor= ale1
print(f' num. sorteado foram {ale1} {ale2} {ale3} {ale4}')
if ale1 > ale2:
    maior= ale1
elif ale3> maior:
    maior=ale3
elif ale4> maior:
    maior=ale4
if ale1 < ale2:
    menor= ale1
elif ale3< maior:
    menor=ale3
elif ale4< maior:
    menor=ale4
print(f'o maior é {maior}')
print(f'o menor número é {menor}')

