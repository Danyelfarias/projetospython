def fato(n):
    f=1
    for num in range(1,n+1):
        f*=num
    return f

numero= int(input('digite um numro: '))   
resp=fato(numero)
print(resp)


