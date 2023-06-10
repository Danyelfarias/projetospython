from datetime import date

data = [28, 4, 2023]

a = int(input("Digite o dia em que você nasceu: "))
b = int(input("Digite o mês em que você nasceu: "))
c = int(input("Digite o ano em que você nasceu: "))

data_nascimento = date(c, b, a)
hoje = date.today()

idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))#nao estendi essa parte do comando
#consequentemente nao entedi todo o resto

if idade >= 18:
    ano_alistamento = data_nascimento.year + 18
    print("Você já deveria ter se alistado em {}.".format(ano_alistamento))
else:
    anos_faltantes = 18 - idade
    ano_alistamento = data_nascimento.year + 18
    print("Ainda faltam {} anos para você se alistar. Seu alistamento será em {}.".format(anos_faltantes, ano_alistamento))
    
