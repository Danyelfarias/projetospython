velociade= int(input(" qual é sua velociade? "))
multa= 7
#custo_da_multa= velociade - 80
if velociade < 80 : 
    print( "sua velociade ainda esta abaixo do limite ")
else:
    print("sua velociade esta acima do permitido")
    print(f" vc foi multado em {(velociade - 80)*multa} ")
