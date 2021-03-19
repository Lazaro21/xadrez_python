from abc import ABCMeta, abstractmethod
from enum import Enum


class Cores(Enum):

    BRANCA = 0
    PRETA = 1


class Peca(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, posicao, cor, tabuleiro):
        self.linha = posicao.linha
        self.coluna = posicao.coluna
        self.COR = cor
        self.tabuleiro = tabuleiro
        self.qtde_movimentos = 0

    @abstractmethod
    def movimentos_possiveis(self):
        pass

    @abstractmethod
    def ha_algum_movimento_possivel(self):
        pass
