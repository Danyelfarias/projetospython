# lista = [{'nome': 'o'}, {'gols': []}, {'total': ''}]
# lista[0]['nome'] = str(input('Nome: '))
# numero_jogos = int(input('Quantos jogos ele fez: '))

# cont = 0
# total = 0
# lista_gols = []
# for gol in range(numero_jogos):
#     gol = int(input(f'Quantos gols na rodada {cont+1}: '))
#     lista_gols.append(gol)
#     cont = cont + 1
#     total = total + gol

# lista[1]['gols'] = lista_gols
# lista[2]['total'] = total
# print(lista)

# for i, atleta in enumerate(lista):
#     print(f"\nDados do atleta {i+1}:")
#     print("Nome:", atleta['nome'])
#     print("Gols por rodada:", atleta['gols'])
#     print("Total de gols:", atleta['total'])

lista = [{'nome': ''}, {'gols': []}, {'total': ''}]
lista[0]['nome'] = str(input('Nome: '))
numero_jogos = int(input('Quantos jogos ele fez: '))

cont = 0
total = 0
lista_gols = []
for gol in range(numero_jogos):
    gol = int(input(f'Quantos gols na rodada {cont+1}: '))
    lista_gols.append(gol)
    cont = cont + 1
    total = total + gol

lista[1]['gols'] = lista_gols
lista[2]['total'] = total
print(lista)

for i, atleta in enumerate(lista):
    if i == 0:
        print('Nome:', atleta['nome'])
    elif i == 1:
        print("Gols por rodada:", atleta['gols'])
    elif i == 2:
        print("Total de gols:", atleta['total'])
