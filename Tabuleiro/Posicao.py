


class Posicao:

    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    def alterar_valores(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    def __str__(self):
        return f"(L{self.linha}, C{self.coluna})"

