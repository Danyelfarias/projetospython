import random
print("1-pedra , 2- papel , 3 - tesoura")
minha_escolha= input("pedra ,papel ,ou tesoura? ")
escolhas_pc=[1,2,3]
#1 vence 3 e perde 2
#2 vence 1 perde 3
#3 vence 2 perde 1
escolhido_pc=random.choice(escolhas_pc)
if minha_escolha==1 and escolhido_pc== 3:
    print("pedra vence tesoura , vc ganhou ")
elif minha_escolha==1 and escolhido_pc==2:
    print("pedra perde de papel , vc perdeu")
elif minha_escolha==2 and escolhido_pc==1:
    print("papel ganha de pedra , vc ganhou")
elif minha_escolha==2 and escolhido_pc==3:
    print("papel perde de tesoura , vc perdeu")
elif minha_escolha==3 and escolhido_pc==2:
    print("tesoura ganha de papel, vc ganhou")
elif minha_escolha==3 and escolhido_pc==1:
    print("tesoura perde de pedra , vc perdeu")
else:
    print("empate")
#chat gpt
import random

escolhas = ['pedra', 'papel', 'tesoura']
resultados = {
    ('pedra', 'papel'): 'papel',
    ('pedra', 'tesoura'): 'pedra',
    ('papel', 'tesoura'): 'tesoura'
}

while True:
    print("Escolha: 1 - pedra, 2 - papel, 3 - tesoura, 4 - sair")
    minha_escolha = int(input("Digite sua escolha: "))
    if minha_escolha == 4:
        break
    elif minha_escolha < 1 or minha_escolha > 3:
        print("Escolha inválida!")
        continue

    minha_escolha = escolhas[minha_escolha - 1]
    escolhido_pc = random.choice(escolhas)
    print(f"Você escolheu {minha_escolha} e o computador escolheu {escolhido_pc}")
    
    if minha_escolha == escolhido_pc:
        print("Empate!")
    elif (minha_escolha, escolhido_pc) in resultados:
        print(f"Você ganhou! {minha_escolha} ganha de {escolhido_pc}")
    else:
        print(f"Você perdeu! {escolhido_pc} ganha de {minha_escolha}")
