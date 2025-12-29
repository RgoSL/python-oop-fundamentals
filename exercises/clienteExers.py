# Arquivo Com Exercícios do Curso Para Fixação do Módulo de Construtores e Instâncias de Objetos 

# 5
class Cliente:
    def __init__(self, Nome, Sobrenome, Idade, EstadoCivil):
        self.nome = Nome
        self.sobrenome = Sobrenome
        self.idade = Idade
        self.estadoCivil = EstadoCivil

cliente01 = Cliente("Mariana", "Santos", 19, "Solteira")
cliente02 = Cliente("Juliane", "Gomes", 22, "Solteira")
cliente03 = Cliente("Iasmin", "Souza", 17, "Solteira")