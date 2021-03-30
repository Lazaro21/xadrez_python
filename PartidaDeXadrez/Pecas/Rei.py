from JogoDeTabuleiro.PecaXadrez import Peca
from JogoDeTabuleiro.Tabuleiro import Tabuleiro
from JogoDeTabuleiro.Posicao import Posicao


class Rei(Peca):
    
    def __init__(self, posicao, tabuleiro, COR):
        super(Rei, self).__init__(posicao, tabuleiro, COR)

    def __str__(self):
        return " R "
    
    def pode_mover(self, posicao_destino):
        peca_na_posicao_de_destino = self.tabuleiro.peca(posicao_destino)
        return peca_na_posicao_de_destino is None \
            or peca_na_posicao_de_destino.COR != self.COR
    
    def jogadas_possiveis(self):
        movimentos_possiveis = [[False for i in range(8)] for j in range(8)]
        p = Posicao(self.posicao.linha + 8, self.posicao.coluna)

        # acima
        p.linha -= 1
        if self.pode_mover(p):
            movimentos_possiveis[p.linha][p.coluna] = True
        
        # noroeste
        p = Posicao(self.posicao.linha - 1 + 8, self.posicao.coluna - 1)
        if self.pode_mover(p):
            movimentos_possiveis[p.linha][p.coluna] = True
            
        # esquerda
        p = Posicao(self.posicao.linha + 8, self.posicao.coluna - 1)
        if self.pode_mover(p):
            movimentos_possiveis[p.linha][p.coluna] = True
        
        # sudoeste
        p = Posicao(self.posicao.linha + 1 + 7, self.posicao.coluna - 1)
        if self.pode_mover(p):
            movimentos_possiveis[p.linha][p.coluna] = True
            
        # abaixo
        p = Posicao(self.posicao.linha + 1 + 8, self.posicao.coluna)
        if self.pode_mover(p):
            movimentos_possiveis[p.linha][p.coluna] = True
        
        # sudeste
        p = Posicao(self.posicao.linha + 1 + 8, self.posicao.coluna + 1)
        if self.pode_mover(p):
            movimentos_possiveis[p.linha][p.coluna] = True
        
        # direita
        p = Posicao(self.posicao.linha + 8, self.posicao.coluna + 1)
        if self.pode_mover(p):
            movimentos_possiveis[p.linha][p.coluna] = True
            
        # nordeste
        p = Posicao(self.posicao.linha - 1 + 8, self.posicao.coluna + 1)
        if self.pode_mover(p):
            movimentos_possiveis[p.linha][p.coluna] = True

        return movimentos_possiveis
        
                    
        
         
                
        
        