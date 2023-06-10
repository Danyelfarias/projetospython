casa= float(input("valor da casa: "))
salario = float (input(" seu salario? "))
anos_da_prestaçao= int(input("qual é quantidade de anos que vc quer parcelar ? "))
prestaçao = casa/(anos_da_prestaçao*12)
if prestaçao > 0.3*salario:
    print("nao esta tem saldo disponivel para comprar")
else:
    print( f"saldo disponivel para compar a casa , vc vai pagar {anos_da_prestaçao*12} de {prestaçao}")
