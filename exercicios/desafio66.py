while True:#essa sentença significa , 'enquanto a senteça toda for vdd repete ela'
    n = int(input('De qual tabuada você quer saber (digite -9 para sair): '))
    
    if n == -9:
        break

    for t in range(1, 11):
        mult = n * t
        print(f'{n} x {t} = {mult}')
