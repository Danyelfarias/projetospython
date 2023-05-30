import random
numeros=[ 1,2,3,4,5,6,7,8,9,10]
pc=random.choice(numeros)
meu_numero=int(input('escolha um número de 1 a 10: '))
while pc!=meu_numero:
    if pc>meu_numero:
         meu_numero=int(input('número errado, escolha um número maior: '))
    elif pc< meu_numero:
         meu_numero=int(input('número errado,escolhar um número menor'))
   
print('número correto vc adivinhou exatamento o número ')
