from JogoDeTabuleiro.PecaXadrez import Cores


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
    for i in range(tabuleiro.linhas):
        print(8 - i, ": ", end='')
        for j in range(tabuleiro.colunas):
            if tabuleiro[i][j] is None:
                print(' - ', end='')
            else:
                if tabuleiro[i][j].COR == Cores.BRANCA:
                    print(str(tabuleiro[i][j]), end='')
                else:
                    print(bcolors.OKBLUE + str(tabuleiro[i][j]) + bcolors.ENDC, end='')
        print("\n")
    print("     a  b  c  d  e  f  g  h")

