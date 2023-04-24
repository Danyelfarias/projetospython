numero = int(input("Digite um número de 1 a 100: "))
centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

print(f"Centena: {centenas}")
print(f"Dezena: {dezenas}")
print(f"Unidade: {unidades}")


