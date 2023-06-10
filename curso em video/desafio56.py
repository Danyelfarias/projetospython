cont=0
somaidade=0
contmulheres=0
for pessoas in range(1,5):
    
    nome=input('nome: ')
    idade=int(input('idade: '))
    sexo=str(input(" sexo[M\F]")).upper()  
    cont=cont+1
    somaidade=somaidade+idade
    # sexoupper=sexo.upper()
    print(f'----------{cont}-----------')
    print(f'nome: {nome}')
    print(f'idade {idade}')
    print(f'sexo {sexo}')
    if sexo=='F' and idade<= 20:
        contmulheres=contmulheres+1
media= somaidade/cont
print(f'a media das idade é {media}')
print(f'ao todo são {contmulheres} com menos de 20 anos')

