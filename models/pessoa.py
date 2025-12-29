# Arquivo Com Exercícios do Curso Para Fixação do Módulo de Property e Métodos de Classe

class Pessoa:
    def __init__(self, nome = '', idade = 0, profissao = ''):
        self.Nome = nome
        self.Idade = idade
        self.Profissao = profissao

    def __str__(self):
        return f'{self.Nome}, {self.Idade} anos, {self.Profissao}'

    @property
    def saudacao(self):
        if self.Profissao:
            return f'Olá, me chamo {self.Nome}! Sou {self.Profissao}.'
        else:
            return f'Olá, sou {self.Nome}!'

    def aniversario(self):
        self.Idade += 1
        
pessoa1 = Pessoa(nome = 'Alberto', idade = 34, profissao = 'Pedreiro')
pessoa2 = Pessoa(nome = 'Marcelo', idade = 47, profissao = 'Arquiteto')
pessoa3 = Pessoa(nome = 'Sebastião', idade = 21)

print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa3.aniversario()

print("Após o Aniversário:")
print(pessoa1)
print(pessoa3)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)