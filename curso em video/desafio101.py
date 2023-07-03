def voto(a):
    if a>18:
        print('vota')
    else:
        print('nao voto')
    return a

b=int(input('qual é sua idade: '))
cat= voto(b)