from JogoDeTabuleiro.Tabuleiro import Tabuleiro
from JogoDeTabuleiro.PecaXadrez import Cores
from JogoDeTabuleiro.Posicao import Posicao
from PartidaDeXadrez.Pecas.Rei import Rei
from PartidaDeXadrez.Pecas.Torre import Torre


class JogoXadrez:

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.inicializacao_do_jogo()

    def adicionar_nova_peca(self, peca, posicao):
        self.tabuleiro.colocar_peca(peca, posicao)

    def inicializacao_do_jogo(self):
        self.adicionar_nova_peca(Rei(Posicao(2, 1), Cores.BRANCA, self.tabuleiro), Posicao(2, 1))
        self.adicionar_nova_peca(Torre(Posicao(0, 4), Cores.PRETA, self.tabuleiro), Posicao(0, 4))
        self.adicionar_nova_peca(Torre(Posicao(7, 4), Cores.PRETA, self.tabuleiro), Posicao(7, 4))


class XadrezException(Exception):
    """Responsável por lancar excecões relativas a lógica do jogo de xadrez"""
    pass
