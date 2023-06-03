
cont=0
soma=0
while True:
    num=int(input('digite um numero '))
    if num==999:
        break
    cont+=1
    soma+=num

print(f'a soma dos {cont} números é {soma} ')

print('encerrado')

