from abc import ABCMeta, abstractmethod
from enum import Enum


class Cores(Enum):

    BRANCA = 0
    PRETA = 1


class Peca(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, posicao, cor, tabuleiro):
        self.posicao = posicao
        self.COR = cor
        self.tabuleiro = tabuleiro
        self.qtde_movimentos = 0

    @abstractmethod
    def jogadas_possiveis(self):
        pass

    def jogada_possivel(self, posicao):
        possiveis = self.jogadas_possiveis()
        return possiveis[posicao.linha][posicao.coluna]

    def ha_alguma_jogada_possivel(self):
        possiveis = self.jogadas_possiveis()
        for i in possiveis:
            for j in possiveis:
                if j:
                    return j

    def ha_uma_peca_oponente_nesta_posicao(self, posicao):
        peca_posicao_especificada = self.tabuleiro.peca(posicao)
        if peca_posicao_especificada is not None and peca_posicao_especificada.COR != self.COR:
            return True

