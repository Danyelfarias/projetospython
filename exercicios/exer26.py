#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
palavra = str(input(" coloque uma palavra: "))
quant_a = palavra.count("a")
print(f"{quant_a}")
