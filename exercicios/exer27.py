nome= input("qual é o seu nome :" )
silva= nome.find("silva",0 , len(nome))
if silva ==-1 :
    print("nao possui o nome silva")
else:
    print("possui o nome silva")
#metodo guanabara
nome = input("Qual é o seu nome: ") #strip()
print("silva" in nome.lower())
