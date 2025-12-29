# Arquivo Para Consolidar o Conteúdo do Módulo de Construtores e Instâncias de Objetos 

class Restaurante:
    restaurantes = [] 
    
    def __init__(self, Nome, Categoria): 
        self._Nome = Nome.title() # Função Nativa Utilizada Para Deixar as Iniciais Maiúsculas
        self._Categoria = Categoria.upper() # Função Nativa Para Deixar Todas as Letras Maiúsculas
        self._Ativo = False
        Restaurante.restaurantes.append(self) 
    
    # Método Especial do Python Para Conversão do Objeto Para Strings
    def __str__(self):
        return f'Nome : {self._Nome} - Categoria : {self._Categoria}'
    
    # Indicador de Que Esse Método Pertence Especificamente a Essa Classe 
    @classmethod 
    def listar_restaurante(cls): 
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._Nome.ljust(25)} | {restaurante._Categoria.ljust(25)} | {restaurante.Ativo}')
            
    # Decorator Para Mudar a Forma Como um Atributo é Lido
    @property
    def Ativo(self):
        return '☑️' if self._Ativo else '🟪'
    
    def alternar_estado(self):
        self._Ativo = not self._Ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'Italiana')

Restaurante.listar_restaurante()