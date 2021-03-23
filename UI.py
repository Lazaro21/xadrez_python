from JogoDeTabuleiro.PecaXadrez import Cores
from JogoDeTabuleiro.Posicao import Posicao
import os
import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def imprimir_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro.tabuleiro)):
        print(8 - i, ": ", end='')
        for j in range(len(tabuleiro.tabuleiro)):
            if tabuleiro.tabuleiro[i][j] is None:
                print(' - ', end='')
            else:
                if tabuleiro.tabuleiro[i][j].COR == Cores.BRANCA:
                    print(str(tabuleiro.tabuleiro[i][j]), end='')
                else:
                    print(bcolors.OKBLUE + str(tabuleiro.tabuleiro[i][j]) + bcolors.ENDC, end='')
        print("\n")
    print("     a  b  c  d  e  f  g  h")


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
