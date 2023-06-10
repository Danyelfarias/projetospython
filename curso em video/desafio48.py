soma=0#atua como um contador , ele vai começar como zero mas no final da função ele vai crescendo
cont=0# esse vai atuar como um contador de termos , diferete do soma que conta os valores
for divisivel3 in range(0,500):
    if divisivel3 % 3==0:
        soma= soma + divisivel3
        cont=cont+1
print(soma)
