import random
aposta= int(input("qual numero vc acha que eu estou pensando: "))
lista=[1,2,3,4,5,6]
escolhido= random.choice(lista)
if aposta== escolhido:
    print(f"sim , vc acetou eu escolhim {escolhido} ")
else :
  print(f"vc errou, eu escolhi o numero \033[93;104m{escolhido}\033[0m")

