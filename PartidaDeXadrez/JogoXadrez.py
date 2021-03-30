from JogoDeTabuleiro.Tabuleiro import Tabuleiro, TabuleiroException
from JogoDeTabuleiro.PecaXadrez import Cores
from JogoDeTabuleiro.Posicao import Posicao
from PartidaDeXadrez.Pecas.Rei import Rei
from PartidaDeXadrez.Pecas.Torre import Torre


class JogoXadrez:

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.inicializacao_do_jogo()
        self.pecas_capturadas = []
        self.turno = 1
        self.jogador_atual = Cores.BRANCA

    def adicionar_nova_peca(self, peca, posicao):
        self.tabuleiro.colocar_peca(peca, posicao)

    def realizar_jogada_de_xadrez(self, origem, destino):
        self.validar_posicao_de_destino(origem, destino)
        self.validar_posicao_de_origem(origem)
        peca_capturada= self.realizar_jogada(origem, destino)
        if peca_capturada is not None:
            self.pecas_capturadas.append(peca_capturada)
        self.proximo_turno()
        return peca_capturada

    def realizar_jogada(self, origem, destino):
        peca_movida = self.tabuleiro.remover_peca(origem)
        peca_capturada = self.tabuleiro.remover_peca(destino)
        self.adicionar_nova_peca(peca_movida, destino)
        return peca_capturada

    def validar_posicao_de_destino(self, origem, destino):
        if not self.tabuleiro.peca(origem).jogada_possivel(destino):
            raise XadrezException("A peca escolhida não pode ser mover para a posicão escolhida. ")

    def validar_posicao_de_origem(self, origem):
        if not self.tabuleiro.ha_uma_peca_nessa_posicao(origem):
            raise XadrezException("Não há uma peca na posicão escolhida. ")
        if self.jogador_atual != self.tabuleiro.peca(origem).COR:
            raise XadrezException("A peca escolhida não é sua.")
        if not self.tabuleiro.peca(origem).ha_alguma_jogada_possivel():
            raise XadrezException("Não há movimentos possíveis para a peca escolhida. ")

    def jogadas_possiveis(self, posicao):
        self.validar_posicao_de_origem(posicao)
        return self.tabuleiro.peca(posicao).jogadas_possiveis()
    
    def proximo_turno(self):
        self.turno += 1
        if self.jogador_atual == Cores.BRANCA:
            self.jogador_atual = Cores.PRETA
        else:
            self.jogador_atual = Cores.BRANCA

    def inicializacao_do_jogo(self):
        self.adicionar_nova_peca(Rei(Posicao(2, 1), Cores.BRANCA,
                                     self.tabuleiro), Posicao(2, 1))

        self.adicionar_nova_peca(Rei(Posicao(1, 2), Cores.PRETA,
                                     self.tabuleiro), Posicao(1, 2))

        self.adicionar_nova_peca(Torre(Posicao(0, 4), Cores.PRETA,
                                       self.tabuleiro), Posicao(0, 4))

        self.adicionar_nova_peca(Torre(Posicao(7, 3), Cores.BRANCA,
                                       self.tabuleiro), Posicao(7, 3))

        self.adicionar_nova_peca(Torre(Posicao(3, 5), Cores.PRETA,
                                       self.tabuleiro), Posicao(3, 5))

        self.adicionar_nova_peca(Torre(Posicao(2, 4), Cores.BRANCA,
                                       self.tabuleiro), Posicao(2, 4))

        self.adicionar_nova_peca(Torre(Posicao(0, 1), Cores.PRETA,
                                       self.tabuleiro), Posicao(0, 1))

        self.adicionar_nova_peca(Torre(Posicao(2, 7), Cores.BRANCA,
                                       self.tabuleiro), Posicao(2, 7))


class XadrezException(TabuleiroException):
    """Responsável por lancar excecões relativas a lógica do jogo de xadrez"""
    pass
