# Arquivo Para Consolidar o Conteúdo do Módulo de Importando Classes e Composição

from models.restauranteExpo import Restaurante

restaurante_japones = Restaurante('Sapporo', 'Japonesa')
restaurante_japones.receber_avaliacao('Thaís', 5.0)
restaurante_japones.receber_avaliacao('Davy', 3.0)
restaurante_japones.receber_avaliacao('Micalli', 4.5)

def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()