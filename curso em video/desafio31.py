#0,50 cada km rodado ate 200 km
#0,45 para viagem acima de 200 km
kilometragem = float(input(" qual é tamanho da sua viagem?"))
abaixo200= 0.50*kilometragem
acima200= 0.45*kilometragem
if kilometragem < 201 :
   print (f" o preço da viagem fica {abaixo200:.2f}")
else:
   print(f"o preço da sua passagem fica {acima200:.2f}")