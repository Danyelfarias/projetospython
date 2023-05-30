sexo = str(input('digite o seu sexo: ')).strip().upper()[0]
while sexo not in 'fFMf' :
    sexo=str(input('codigo invalido por favor digitar novamente')).strip().upper()[0]
if sexo=='M':
    sexo='MASCULINO'
elif sexo=='F':
    sexo='FEMININO'

print(f'seu sexo é {sexo}')

