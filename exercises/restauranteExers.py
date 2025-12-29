# Arquivo Com Exercícios do Curso Para Fixação do Módulo de Classes

from models.restaurante import  restaurante_praca, Restaurante

# 1-
restaurante_praca.Categoria = "Italiana"

# 2-
print(restaurante_praca.Nome)

# 3-
if restaurante_praca.Ativo == True :
    print("O Restaurante Está Ativo")
else:
    print("O Restaurante Está Desativado")

# 4-
Categoria = Restaurante.Categoria
print(f"{Categoria}")

# 5-
restaurante_praca.Nome = "Bistrô"

# 6-
restaurante_pizza = Restaurante()

restaurante_pizza.Nome = "Pizza Place"
restaurante_pizza.Categoria = "Fast Food"

# 7-
if restaurante_pizza.Categoria == "Fast Food":
    print("A Categoria Desse Restaurante é Fast Food")
else:
    print("A Categoria Desse Restaurante Não é Fast Food")

# 8-
restaurante_pizza.Ativo = True

# 9-
print(f"Objeto 'restaurante_praca': {restaurante_praca.Nome}, {restaurante_praca.Categoria}")