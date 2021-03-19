class UI:

    def imprimir_tabuleiro(self, tabuleiro):
        for i in range(tabuleiro.linhas):
            for j in range(tabuleiro.colunas):
                self.imprimir_peca(tabuleiro[i][j])
            print("\n")
        print("  a b c d e f g")


    def imprimir_peca(self, peca):
        if peca is None:
            print('-')
        else:
            print(peca)
        print(" ")