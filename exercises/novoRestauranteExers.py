# Arquivo Com Exercícios do Curso Para Fixação do Módulo de Construtores e Instâncias de Objetos 

# 2
class Restaurante:
    Nome = ""
    Categoria = ""
    Ativo = False
    Endereco = ""
    Avaliacao = int
    
madero = Restaurante()

madero.Avaliacao = 5
madero.Nome = "Madero Restaurante"
madero.Categoria = "Hamburgueria"
madero.Endereco = "Av. Aricanduva, 5555 - Jardim Marília, São Paulo"

# 3
class Restaurante:
    def __init__(self, Nome="", Categoria="", Ativo=False):
        self.nome = Nome
        self.categoria = Categoria
        self.ativo = Ativo
        
madero = Restaurante("Madero Restaurante", "Hamburgueria")

# 4
    def __str__(self):
        return f'Nome : {self.nome} - Categoria : {self.categoria}'

novoRestaurante = Restaurante(Nome = "Divino Fogão", Categoria = "Fazenda")
print(novoRestaurante)