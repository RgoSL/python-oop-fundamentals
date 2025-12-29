# Arquivo Com Exercícios do Curso Para Fixação do Módulo de Importando Classes e Composição

# 5
from livroExers import Livro

# 6
livro04 = Livro("A Morte de Ivan Ilitch", "Liev Tostói", 1886)
print(f"Em Estoque: {livro04.disponivel}")
livro04.emprestar()
print(f"Em Estoque: {livro04.disponivel}")

# 7 
ano_especifico = 2024
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")