# Arquivo Para Consolidar o Conteúdo do Módulo de Importando Classes e Composição

from models.avaliacao import Avaliacao

class Restaurante:
    restaurantes = [] 
    
    def __init__(self, Nome, Categoria): 
        self._Nome = Nome.title() # Função Nativa Utilizada Para Deixar as Iniciais Maiúsculas
        self._Categoria = Categoria.upper() # Função Nativa Para Deixar Todas as Letras Maiúsculas
        self._Ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self) 
    
    # Método Especial do Python Para Conversão do Objeto Para Strings
    def __str__(self):
        return f'Nome : {self._Nome} - Categoria : {self._Categoria}'
    
    # Indicador de Que Esse Método é Utilizado Pela Classe Inteira
    @classmethod 
    def listar_restaurante(cls): 
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._Nome.ljust(25)} | {restaurante._Categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.Ativo}')
            
    # Decorator Para Mudar a Forma Como um Atributo é Lido
    @property
    def Ativo(self):
        return '☑️' if self._Ativo else '🟪'
    
    def alternar_estado(self):
        self._Ativo = not self._Ativo
        
    def receber_avaliacao(self, cliente, nota):
        if nota > 0 and nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Restaurante Inédito!'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantida_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantida_de_notas, 1)
        return media