nome= input(" coloque seu nome completo: ")
nome_maiusculo= nome.upper()
nome_minusculo= nome.lower()
quantidade_letras= len(nome.strip())
quantidade_nome= len(nome.split()[0])
#a funçao spliter tem sempre que vim acompanhada dos chochetes "[]" para mostar qual termo ele quer assumir
primeiro_nome= nome.split()[0]
print(f"SEU NOME É  EM CAIXA ALTA É {nome_maiusculo}")
print(F" SEU NOME MINUSCULO É: {nome_minusculo}")
print(F"SEU NOME TEM {quantidade_letras} LETRAS")
print(F"SEU PRIMERIO NOME É {primeiro_nome} E POSSUI {quantidade_nome} LETRS ")