from datetime import date

cont = 0
cont2 = 0
ano = date.today().year
for veses in range(0,5):
 idade = int(input(f"Ano de nascimento da {veses+1} pessoa: "))
 if ano - idade >= 18:
   cont += 1
 else:
   cont2 += 1
print(f"{cont} pessoas são maiores de idade e {cont2} pessoas são menores de idade.")
