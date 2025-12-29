# Classe Principal Com o Modelo de Músicas
class Musica:
    musicas = [] # Criação de Uma Lista Para Guardar as Músicas Criadas
    
    # Método Especial do Python Indicando um Construtor Que Espera Informações Específicas
    def __init__(self, Nome, Artista, Duracao): # Convenção Self Para Indicar a Instância Atual
        self.nome = Nome # Indica Que Esse Objeto Recebe o Parâmetro do Construtor
        self.artista = Artista
        self.duracao = Duracao
        Musica.musicas.append(self) # Definindo Que a Lista Recebe Cada Instância da Classe
        
    # Método Autoral Para a Apresentação de Todas as Músicas da Classe
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'Música: {musica.nome} | Artista: {musica.artista} | Duração: {musica.duracao} segundos.')

# Instâncias da Classe Música Com Parâmetros Obrigatórios       
musica02 = Musica("Ela Partiu", "Tim Maia", 256)
musica01 = Musica("Modo de Dizer", "Jão", 177)

# "Print" Substítuido Pela Chamada da Função de Listagem
Musica.listar_musicas()