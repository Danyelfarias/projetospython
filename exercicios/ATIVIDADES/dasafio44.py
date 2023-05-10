preço= float(input("qual é o valor do produto: "))
print("1 - avista  2-avista no cartao  3- 2x no cartão  4 - 3x no cartão  ")
metodo_de_pagamento= int((input(" como vc deseja pagar: ")))
avista= preço*0.90
avista_no_cartão= preço*0.95
duas_veses_no_cartão= preço/2
tres_veses_no_cartao= (preço*1.2)/3
if metodo_de_pagamento == 1:
    print(f"vc ter um desconto de 10% ,vai pagar apenas: {avista:2f} ")
elif metodo_de_pagamento==2:
    print(f"voce tem um desconto de 5%, vai pagar apenas: {avista_no_cartão:2f}")
elif(metodo_de_pagamento==3):
    print(f"vai duas pacelas de {duas_veses_no_cartão:.2f}")
elif(metodo_de_pagamento== 4):
    print(f"vc vai pagar tres parcelas de {tres_veses_no_cartao:.2f}")
else:
    print("metodo de pagamento nao reconhecido")
