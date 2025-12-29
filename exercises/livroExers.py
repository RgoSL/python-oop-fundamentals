# Arquivo Com Exercícios do Curso Para Fixação do Módulo de Importando Classes e Composição

# 1
class Livro():
    def __init__(self, titulo, autor, anoPubli, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.anoPubli = anoPubli
        self.disponivel = disponivel
        
# 2
    def __str__(self):
        return f'Livro: {self.titulo} de {self.autor} - {self.anoPubli}'
    
livro01 = Livro('Pequeno Príncipe', 'Antoine de Saint', 1943)
livro02 = Livro('Adorável Cretino', 'Camila Ferreira', 2015)

print(livro01)
print(livro02)

# 3
    def emprestar(self):
        self.disponivel = not self.disponivel

livro03 = Livro('Felicidade ou Morte', 'Clóvis de Barros', 2016)
livro03.emprestar()

# 4
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.anoPubli == ano and livro.disponivel]
        return livros_disponiveis

Livro.livros = [livro01, livro02, livro03]