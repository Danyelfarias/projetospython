numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
quantidade=len(numeros_extenso)
# print( quantidade)
while True:
    escolha=int(input('escolha um número '))
    if escolha<0 or escolha> quantidade:
        print('nuemro nao encontrado')
    else:
        print(f'seu número é {numeros_extenso[escolha]}')
