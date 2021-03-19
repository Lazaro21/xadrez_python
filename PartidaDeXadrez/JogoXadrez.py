from JogoDeTabuleiro.Tabuleiro import Tabuleiro
from JogoDeTabuleiro.PecaXadrez import Cores
from JogoDeTabuleiro.Posicao import Posicao
from PartidaDeXadrez.Pecas.Rei import Rei
from PartidaDeXadrez.Pecas.Torre import Torre


class JogoXadrez:

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.inicializacao_do_jogo()

    def inicializacao_do_jogo(self):
        self.tabuleiro.colocar_peca(Rei(Posicao(2, 1), Cores.BRANCA, self.tabuleiro), Posicao(2, 1))
        self.tabuleiro.colocar_peca(Torre(Posicao(0, 4), Cores.PRETA, self.tabuleiro), Posicao(0, 4))
        self.tabuleiro.colocar_peca(Torre(Posicao(7, 4), Cores.PRETA, self.tabuleiro), Posicao(7, 4))