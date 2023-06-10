palavras=("aparelho","lua","sol","armazen","testando","mandioca")
for pala in palavras:
    print(f'\n pa palavra {pala} tem ')
    for letras in pala:
        if letras.lower() in 'aeiou ' :
            print( letras, end='')
    