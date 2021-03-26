from JogoDeTabuleiro.PecaXadrez import Peca
from JogoDeTabuleiro.Tabuleiro import Tabuleiro
from JogoDeTabuleiro.Posicao import Posicao


class Torre(Peca):

    def __init__(self, posicao, tabuleiro, COR):
        super().__init__(posicao, tabuleiro, COR)

    def __str__(self):
        return " T "

    def jogadas_possiveis(self):
        movimentos_possiveis = [[None for i in range(8)] for j in range(8)]
        p = Posicao(0, 0)

        # acima
        p.linha = self.posicao.linha - 1
        p.coluna = self.posicao.coluna
        while Tabuleiro.posicao_existe(p) and not self.tabuleiro.ha_uma_peca_nessa_posicao(p):
            movimentos_possiveis[p.linha][p.coluna] = True
            p.linha -= 1

        if Tabuleiro.posicao_existe(p) and self.ha_uma_peca_oponente_nesta_posicao(p):
            movimentos_possiveis[p.linha][p.coluna] = True

        # esquerda
        p.linha = self.posicao.linha
        p.coluna = self.posicao.coluna - 1
        while Tabuleiro.posicao_existe(p) and not self.tabuleiro.ha_uma_peca_nessa_posicao(p):
            movimentos_possiveis[p.linha][p.coluna] = True
            p.coluna -= 1

        if Tabuleiro.posicao_existe(p) and self.ha_uma_peca_oponente_nesta_posicao(p):
            movimentos_possiveis[p.linha][p.coluna] = True

        # baixo
        p.linha = self.posicao.linha + 1
        p.coluna = self.posicao.coluna
        while Tabuleiro.posicao_existe(p) and not self.tabuleiro.ha_uma_peca_nessa_posicao(p):
            movimentos_possiveis[p.linha][p.coluna] = True
            p.linha += 1

        if Tabuleiro.posicao_existe(p) and self.ha_uma_peca_oponente_nesta_posicao(p):
            movimentos_possiveis[p.linha][p.coluna] = True

        # direita
        p.linha = self.posicao.linha
        p.coluna = self.posicao.coluna + 1
        while Tabuleiro.posicao_existe(p) and not self.tabuleiro.ha_uma_peca_nessa_posicao(p):
            movimentos_possiveis[p.linha][p.coluna] = True
            p.coluna += 1

        if Tabuleiro.posicao_existe(p) and self.ha_uma_peca_oponente_nesta_posicao(p):
            movimentos_possiveis[p.linha][p.coluna] = True

        return movimentos_possiveis


