def contagem(i,r):
    cont=0 
    lista=[]
    listamenos=[]
    while cont<10:
        lista.append(cont+1)
        cont+=1
    inicial=10
    razao=0
    while inicial>razao:
        variacao= inicial-razao
        listamenos.append(variacao)
        razao+=2
    print('-'*30)
    print(lista)
    print('-'*30)
    print(listamenos)
    listainput=[]
    inicial=i
    razao=r
    while inicial> razao:
        variacao= inicial-razao
        listainput.append(variacao)
        razao+=r
    print('-'*30)
    from time import sleep
    sleep(3)
    print(f'{listainput}',flush=True)
    print('-'*30)

i=int(input('digite um numero: '))
r=int(input('digite a razao: '))
contagem(i,r)
# listamenos=[]
# inicial=10
# razao=0
# while inicial!=0:
#     variacao= inicial-razao
#     listamenos.append(variacao)
#     razao+=2
# print(listamenos)
        