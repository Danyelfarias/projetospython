nome = input("Digite seu nome: ")
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
quantidade_letras = len(nome)
quantidade_letras_sem_espaco = len(nome.strip())
print(f"O nome em letras maiúsculas é {nome_maiusculo}")
print(f"O nome em letras minúsculas é {nome_minusculo}")
print(f"A quantidade total de caracteres é {quantidade_letras}")
print(f"A quantidade de letras (sem espaços) é {quantidade_letras_sem_espaco}")
