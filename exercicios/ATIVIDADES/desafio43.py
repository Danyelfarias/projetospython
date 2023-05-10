peso = float(input("sua peso"))
altura=float(input("sua altura"))
imc=peso/(altura**2)
print(f"seu imc é {imc:.1f}")
if imc <18.5:
    print("abaixo do peso")
elif imc >18.5 and imc<=25:
    print("peso ideal")
elif imc >25 and imc<=30:
    print("sobrepeso 1")
elif imc >30 and imc<=40:
    print("obesidade ")
else:
    print("obesidade morbida")
#comanado feito pelo chat gpt
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / altura ** 2
if imc < 18.5:
    print(f"IMC: {imc:.1f} - abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    print(f"IMC: {imc:.1f} - peso ideal")
elif imc > 25 and imc <= 30:
    print(f"IMC: {imc:.1f} - sobrepeso")
elif imc > 30 and imc <= 40:
    print(f"IMC: {imc:.1f} - obesidade")
else:
    print(f"IMC: {imc:.1f} - obesidade mórbida")

