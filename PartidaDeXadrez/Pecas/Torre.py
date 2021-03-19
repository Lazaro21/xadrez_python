from JogoDeTabuleiro.PecaXadrez import Peca


class Torre(Peca):

    def __init__(self, posicao, tabuleiro, cor):
        super().__init__(posicao, tabuleiro, cor)

    def __str__(self):
        return " T "

    def ha_algum_movimento_possivel(self):
        pass

    def movimentos_possiveis(self):
        pass