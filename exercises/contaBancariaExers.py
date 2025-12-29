# Arquivo Com Exercícios do Curso Para Fixação do Módulo de Property e Métodos de Classe

# 1
class ContaBancaria():
    def __init__(self, titular = '', saldo = 0.0, ativo = False):
        self._Titular = titular
        self._Saldo = saldo
        self._ativo = ativo

# 2
    def __str__(self):
        return f'Titular: {self._Titular}, saldo atual: {self._Saldo:.2f}'

conta01 = ContaBancaria('Eduardo', 543.60)
conta02 = ContaBancaria('Arthur', 232.44)

print(conta01)
print(conta02)

# 3
    def ativar_conta(self):
        self.ativo = not self.ativo
        
conta03 = ContaBancaria('Vinicius', 297.32)
conta03.ativar_conta()
print(conta03)

# 5
conta04 = ContaBancaria('Felipe', 542.55)

print(conta04.self.Titular)