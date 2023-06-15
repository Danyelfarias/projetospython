matrix= [[[],[],[]],[[],[],[]],[[],[],[]]]
cont=0
cont2=0
par=0
inpar=0
for coluna in range(9):
    valores=int(input('digite um número: '))
    matrix[cont][cont2].append(valores)
    cont2=cont2+1
    if valores %2==0:
        par= valores+par
    else:
        inpar = valores+ inpar
    if cont2 ==3:
        cont+=1
        cont2=0
        if cont==1:
            maior=0
            menor=0
            valores>maior
            maior=valores
        else:
            valores<menor
            menor=menor
print(matrix)
tercieracoluna=matrix[2][0] + matrix[2][1] + matrix[2][2]#dessa maneira que eu coloquei nao consegui somar
print(matrix[0][0:3], end=' \n')
print(matrix[1][0:3],end=' \n')
print(matrix[2][0:3],end=' \n')
print(f'as somas dos numero pares é {par}e a soma dos valores inpares é {inpar}')
print(tercieracoluna)
print(f'o maio numro da segunda linha é {maior}')

