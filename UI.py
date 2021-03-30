from JogoDeTabuleiro.PecaXadrez import Cores
from JogoDeTabuleiro.Posicao import Posicao
import os


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = "\033[0;30m"
    BLINK = "\033[5m"


def imprimir_tabuleiro(tabuleiro, movimentos_possiveis = None):
    if movimentos_possiveis is None:
        movimentos_possiveis = [[False for i in range(8)] for j in range(8)]
    for i in range(len(tabuleiro.tabuleiro)):
        print(8 - i, ": ", end='')
        for j in range(len(tabuleiro.tabuleiro)):
            if movimentos_possiveis[i][j]:
                print(Bcolors.BLACK, end='')
            if tabuleiro.tabuleiro[i][j] is None:
                print(' - ' + Bcolors.ENDC, end='')
            else:
                if tabuleiro.tabuleiro[i][j].COR == Cores.BRANCA:
                    if movimentos_possiveis[i][j]:
                        print(Bcolors.OKGREEN + str(tabuleiro.tabuleiro[i][j]), end='')
                    else:
                        print(str(tabuleiro.tabuleiro[i][j]), end='')
                else:
                    if movimentos_possiveis[i][j]:
                        print(Bcolors.OKGREEN + str(tabuleiro.tabuleiro[i][j]), end='')
                    else:
                        print(Bcolors.OKBLUE + str(tabuleiro.tabuleiro[i][j]) + Bcolors.ENDC, end='')
        print("\n")
    print("     a  b  c  d  e  f  g  h")


def imprimir_jogo_de_xadrez(jogo_de_xadrez, movimentos_possiveis = None):
    imprimir_tabuleiro(jogo_de_xadrez.tabuleiro, movimentos_possiveis)
    print()
    print("Turno: ", jogo_de_xadrez.turno)
    print("Esperando a jogada de: ", jogo_de_xadrez.jogador_atual)


def ler_posicao_xadrez(msg):
    try:
        posicao_string = input(msg)
        nova_posicao = Posicao(int(posicao_string[1]), converter_posicao_letra_numero(posicao_string[0]))
        return nova_posicao
    except TypeError:
        print("Posicão não válida. Por favor digite uma posicão no estilo: A-1 até H-8")


def converter_posicao_letra_numero(linha):
    _ = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    return _.get(linha)


def limpar_tela():
    if os.name == "posix":
        # Linux e mac
        _ = os.system('clear')
    else:
        # Windows
        _ = os.system('cls')
