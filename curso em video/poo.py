# class carro:
#     def __unit__(self, nome, estado=False):
#         self.nome=nome
#         self.estado= estado

#     def acelerando (self):
#         self.estado = 'acelerando'


# camaro=carro('camaro')
# camaro.acelerando()
# print(camaro.estado)
class Carro:
    def __init__(self, nome, estado=False):#definou o parametro com false camo ele nao seja definico futuramente
        self.nome = nome#defini self.nome como se fosse apenas uma variavel 
        self.estado = estado#mesma coisa aqui .para nao ter que chamar toda vez esse paramenteo self.estado 

    def acelerando(self):#fazendo funçoes para fazer açoes
        self.estado = 'acelerando'
    def nitro(self):
        self.estado="modo turbo"

    

camaro = Carro('camaro')#definir o nome da memoria 
camaro.acelerando()#definir o "estado" , definir como vai ser ele na memoria.
print(camaro.estado)  # Output: acelerando
camaro.nitro()#mesma coisa redefinind  a memoria
print(camaro.estado)




        