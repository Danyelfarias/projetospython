soma=0
cont=0
for c in range(0,7):
    input(f"digite um valor{c}: ")
    if c%2==0:
     soma= soma+c
     cont= cont+1
print(f"dos {cont} numeros pares citaos a sua soma é {soma}")

