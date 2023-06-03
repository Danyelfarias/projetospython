x=int(input("coloque o número "))
times=int(input("quantos números a frente: "))
y=x-1
z=x-2
cont=0
while times>=cont:   
 if  x!=y+z:
    y-=1
    z-=1
 else:
    k=y+z
    alfa=k+x
    print(f"{k}->{x}->{alfa}")
    cont+=1

