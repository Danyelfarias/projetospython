#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
palavra = input("Digite uma palavra: ")
quant_a = palavra.count("a", 0, len(palavra[0:])) 
#o len nesse caso ai vai mostar o tanto de caracteris,que consequetemente é o tamanho da frase.
primeira = palavra.find("a", 0, len(palavra[0:])) 

if palavra[-1] == "a":
    print("A letra 'a' é a última letra da palavra")
else:
    print("A letra 'a' não é a última letra da palavra")

print(f"A letra 'a' aparece {quant_a} vezes na palavra, pela primeira vez na posição {primeira}")
