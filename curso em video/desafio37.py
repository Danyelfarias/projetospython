numero = int(input("Digite um número inteiro: "))
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)
escolha = input("Escolha um método de conversão: binário, octal ou hexadecimal: ")

if escolha == "binario":
    print("O número em binário é:", binario)
elif escolha == "octal":
    print("O número em octal é:", octal)
elif escolha == "hexadecimal":
    print("O número em hexadecimal é:", hexadecimal)
else:
    print("Escolha inválida!")
