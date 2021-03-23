from JogoDeTabuleiro.PecaXadrez import Peca
from JogoDeTabuleiro.Posicao import Posicao
from UI import imprimir_tabuleiro


class Tabuleiro:

    def __init__(self):
        self.tabuleiro = [[None for i in range(8)] for j in range(8)]
        
    def peca(self, posicao):
        if not self.posicao_existe(posicao):
            raise TabuleiroException("Posicão digitada não existe. ")
        return self.tabuleiro[posicao.linha][posicao.coluna]

    def colocar_peca(self, peca, posicao):
        if self.posicao_existe(posicao):
            if self.ha_uma_peca_nessa_posicao(posicao):
                raise TabuleiroException("Posicão ocupada. ")
            else:
                self.tabuleiro[posicao.linha][posicao.coluna] = peca

    @staticmethod
    def posicao_existe(posicao):
        # print(f"Visualizacão dentro do posicao existe: {posicao.linha - 1}  {posicao.coluna - 1}")
        return 0 <= posicao.linha <= 7 and 0 <= int(posicao.coluna) <= 7

    def ha_uma_peca_nessa_posicao(self, posicao):
        return self.tabuleiro[posicao.linha][posicao.coluna] is not None

    def remover_peca(self, posicao):
        if self.posicao_existe(posicao):
            if self.ha_uma_peca_nessa_posicao(posicao):
                imprimir_tabuleiro(self)
                peca_removida = self.tabuleiro[posicao.linha][posicao.coluna]
                self.tabuleiro[posicao.linha][posicao.coluna] = None
                imprimir_tabuleiro(self)
                return peca_removida
            return None


class TabuleiroException(Exception):
    """Responsável por tratar excecões relacionadas ao tabuleiro"""
    pass

