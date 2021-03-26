from JogoDeTabuleiro.Posicao import Posicao
from JogoDeTabuleiro.Tabuleiro import TabuleiroException
from PartidaDeXadrez.JogoXadrez import JogoXadrez, XadrezException
import UI

p1 = Posicao(0, 5)


def principal():

    jogo_de_xadrez = JogoXadrez()
    UI.imprimir_tabuleiro(jogo_de_xadrez.tabuleiro)
    tabuleiro = jogo_de_xadrez.tabuleiro

    try:
        while True:
            UI.imprimir_tabuleiro(jogo_de_xadrez.tabuleiro)
            print("\n")
            origem = UI.ler_posicao_xadrez("Digite a peca a ser movimentada: ")

            print("\n")
            UI.imprimir_tabuleiro(jogo_de_xadrez.tabuleiro, jogo_de_xadrez.jogadas_possiveis(origem))
            destino = UI.ler_posicao_xadrez("Digite a posicão de destino: ")
            peca_capturada = jogo_de_xadrez.realizar_jogada_de_xadrez(origem, destino)
    except XadrezException as e:
        print(e)
    except TabuleiroException as e:
        print(e)


if __name__ == "__main__":
    principal()