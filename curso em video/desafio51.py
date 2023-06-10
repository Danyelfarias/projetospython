termo=int(input("digite o primerio termo da PA "))
razao=int(input("digite a razão "))
termof= termo+razao*10
for pa in range(termo,termof,razao):
    print(pa,end='-')#usan senpre agaora essa estrutura de end=''
