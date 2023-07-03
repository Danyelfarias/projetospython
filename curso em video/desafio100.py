lista=[]
listapar=[]
def separapar(a):
    par=0
    for n in lista:
        if n% 2==0:
            listapar.append(n)
            par+=n
    print(listapar)
    print(lista)
    print(f'a soma dos numreo pares é {par}')
import random
a=random.randint(0,100)
lista.append(a)
a=random.randint(0,100)
lista.append(a)
a=random.randint(0,100)
lista.append(a)
a=random.randint(0,100)
lista.append(a)
a=random.randint(0,100)
lista.append(a)

separapar(a)




