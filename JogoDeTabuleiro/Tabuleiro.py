from PecaXadrez import Peca
from Posicao import Posicao


class Tabuleiro:

    def __init__(self):
        self.linhas = 8
        self.colunas = 8
        self.pecas = [[] * self.linhas]

    def peca(self, linha, coluna):
        linhas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        linhaNumero = linhas[linha].index()
        return self.pecas[linhaNumero][coluna]