# Arquivo Com Exercícios do Curso Para Fixação do Módulo de Property e Métodos de Classe

# 6
class ClienteBanco():
    
    clientes = []
    
    def __init__(self, nome='', sobrenome='', idade=0, saldo=0.0, vip=False):
        self.Nome = nome
        self.Sobrenome = sobrenome
        self.Idade = idade
        self.Saldo = saldo
        self.Vip = vip
        self.clientes.append(self)
        
# 7
    @classmethod
    def listar_clientes(cls):
        print(f"{'Nome':<15} {'Sobrenome':<15} {'Idade':<10} {'Saldo':<15}")
        print("-" * 55)
        for cliente in cls.clientes:
            print(f"{cliente.Nome:<15} {cliente.Sobrenome:<15} {cliente.Idade:<10} R${cliente.Saldo:<14.2f}")

cliente01 = ClienteBanco('Enzo', 'Costa', 24, 444.52)
cliente02 = ClienteBanco('Gustavo', 'Henrique', 22, 543.11)
cliente03 = ClienteBanco('Jhonattan', 'Alvez', 46, 652.31)

ClienteBanco.listar_clientes()