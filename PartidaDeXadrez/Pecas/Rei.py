from JogoDeTabuleiro.PecaXadrez import Peca


class Rei(Peca):
    
    def __init__(self, posicao, tabuleiro, cor):
        super(Rei, self).__init__(posicao, tabuleiro, cor)

    def __str__(self):
        return " R "

    def ha_alguma_jogada_possivel(self):
        pass

    def jogadas_possiveis(self):
        pass