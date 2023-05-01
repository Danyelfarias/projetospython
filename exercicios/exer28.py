nome = input("Qual é o seu nome completo? ")
nomes = nome.split(" ")

if len(nomes) < 2:
    print("Por favor, insira seu nome completo (com pelo menos duas palavras)")
else:
    primeiro = nomes[0]
    ultimo = nomes[-1]
    print(f"Prazer em te conhecer, {primeiro}!")
    print(f"Seu último nome é {ultimo}.")
    #sobre o metodo len , ele contar a quantidade de termos de uma senteça, podendo ser os termos caracters ou carta plavra de uma lista de frase ,a exempli que quando passa pelo metod "split".
