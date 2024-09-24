# Programa Principal
# Importando o codigo
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avalicao('Gui', 10)
restaurante_praca.receber_avalicao('Lais', 8)
restaurante_praca.receber_avalicao('Emy', 2)

def main():
    Restaurante.listar_restaurantes()

# Para não deixar ser importado por outro script
if __name__ == '__main__':
    main()