# Arquivo Para Fixação do Conceito da Aula 

class Musica: # Criação da Classe Música
    # Definição Dos Atributos da Entidade
    Nome = '' 
    Artista = ''
    Duracao = int
    
# Instâncias da Classe Para 2 Objetos Distintos
musica_theDriver = Musica()
musica_acontece = Musica()

# Definição Dos Valores Específicos de Cada Objeto, Seguindo o Modelo Geral da Classe
musica_theDriver.Nome = "The Driver"
musica_theDriver.Artista = "Maneskin"
musica_theDriver.Duracao = 189

musica_acontece.Nome = "Acontece"
musica_acontece.Artista = "Jão"
musica_acontece.Duracao = 162

# Exibição Dos Atributos do Objeto TheDriver
print(f"Música : {musica_theDriver.Nome} - Banda : {musica_theDriver.Artista} - Duração : {musica_theDriver.Duracao} segundos.")