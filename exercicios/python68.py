
soma=0
while True:
    produto=str(input('QUAL PRODUTO VC QUER COMPRAR: '))
    preço=float(input('PREÇO: '))
    soma+=preço
    print('1-continuar 2-cancelar ')
    comfimaçao= int(input( 'deseja continuar:' ))
    if comfimaçao==2:
            break
print(' compra encerrada')
print( f'o valor das suas compara é de {soma}')
       



    