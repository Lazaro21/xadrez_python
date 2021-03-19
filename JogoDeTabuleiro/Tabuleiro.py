from JogoDeTabuleiro.PecaXadrez import Peca
from JogoDeTabuleiro.Posicao import Posicao


class Tabuleiro(list):

    def __init__(self):
        self.linhas = 8
        self.colunas = 8
        super().__init__([[None for i in range(self.linhas)] for i in range(self.colunas)])

    def peca(self, linha, coluna):
        linhas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        linha_numero = linhas[linha].index()

        if not self.posicao_existe(linha, coluna):
            raise TabuleiroException("Posicão digitada não existe. ")
        return self.pecas[linha_numero][coluna]

    def colocar_peca(self, peca, posicao):
        if self.ha_uma_peca_nessa_posicao(posicao.linha, posicao.coluna):
            raise TabuleiroException("Posicão ocupada. ")

        self[posicao.linha][posicao.coluna] = peca
        peca.posicao = posicao

    @staticmethod
    def posicao_existe(linha, coluna):
        return 0 <= linha <= 7 and 0 <= coluna <= 7

    def ha_uma_peca_nessa_posicao(self, linha, coluna):
        if self.posicao_existe(linha, coluna):
            if self[linha][coluna] is None:
                return True


class TabuleiroException(Exception):
    """Responsável por tratar excecões relacionadas ao jogo de xadrez"""
    pass
