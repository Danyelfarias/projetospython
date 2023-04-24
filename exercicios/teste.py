numero_str = input("Digite um número de 1 a 100: ")
digitos = numero_str.split()

centenas = digitos[0]
dezenas = digitos[1]
unidades = digitos[2]

print(f"Centena: {centenas}")
print(f"Dezena: {dezenas}")
print(f"Unidade: {unidades}")

