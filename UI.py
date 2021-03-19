def imprimir_tabuleiro(tabuleiro):
    for i in range(tabuleiro.linhas):
        print(8 - i, ": ", end='')
        for j in range(tabuleiro.colunas):
            if tabuleiro[i][j] is None:
                print(' - ', end='')
            else:
                print(tabuleiro[i][j], end='')
        print("\n")
    print("     a  b  c  d  e  f  g  h")

