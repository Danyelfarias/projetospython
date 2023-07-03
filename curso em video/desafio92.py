cadastrados= {'nome':"",
            'nsci':'',
            'ano_contrataçao':'',
            'salario':''
            }# o que separa o termo de um dicionario e outro é apenas uma virgurla.
escolha=''
lista=[]
from datetime import datetime
while escolha!='N':
    cadastrados['nome']= str(input('nome: '))
    cadastrados['nsci']= int(input('ano de nascimento: '))
    if datetime.now().year-cadastrados['nsci'] <=18:
        print('essa pessoal n tem 18 anos ainda ')
    else:
        cadastrados['ano_contrataçao']=int(input('ano que esse funicionario foi contratado: '))
        cadastrados['salario']=int(input('qual é a pretençao salarial: '))
        lista.append(cadastrados)
    escolha=str(input(' deseja cadastrar mais alguem: '))

for i,fucionario in enumerate(lista):
    print( 'indice',i)# como enumerate funciona , ele primerio vai chamar a localizaçao , no caso 
    #o indice , depois ele vai chamar outra variavel que chama apenas os compartimanto dos indices 
    # nesse cado ai , chamou nome , ano , salario 
    print('nome', fucionario['nome'])
    print('ano de contrataçao',fucionario['ano_contrataçao'])
    print('salario',fucionario['salario'])

