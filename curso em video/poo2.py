class Pessoa:
    def __init__(self, nome, estado="nao faz nada"):
        self.nome = nome
        self.estado = estado
    
    def comer_muito(self):
        self.estado = "comendo muito"
        print(f"a pessoa {self.nome} {self.estado}")


alta = Pessoa('alta')
alta.comer_muito()

# class Pessoa:
#     def __init__(self, nome, estado="nao faz nada"):
#         self.nome = nome
#         self.estado = estado
    
#     def comer_muito(self):
#         self.estado = "comer muito"
#         print(self.estado)


# alta = Pessoa('alta')
# alta.comer_muito()

