from JogoDeTabuleiro.PecaXadrez import Peca
from JogoDeTabuleiro.Posicao import Posicao


class Tabuleiro(list):

    def __init__(self):
        self.linhas = 8
        self.colunas = 8
        super().__init__([[None for i in range(self.linhas)] for i in range(self.colunas)])

    def peca(self, linha, coluna):
        linhas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        linhaNumero = linhas[linha].index()
        return self.pecas[linhaNumero][coluna]