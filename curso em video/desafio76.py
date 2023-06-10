compras = (
    'arrozf', 4,
    'feijaof', 5,
    'macarrão', 3,
    'manteiga', 2.4
)

for posi in range(0, len(compras)):
    if posi % 2 == 0:
        print(f'{compras[posi]:.<30}', end='')
    else:
        print(f'{compras[posi]:7.2f}')

header = f'{"lista de compras":^45}'
print(header)
print(compras)
