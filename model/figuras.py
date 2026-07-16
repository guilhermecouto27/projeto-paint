from abc import ABC, abstractmethod
import math
from dataclasses import dataclass
# class Figura é uma classe abstrata que define a interface para todas as figuras geométricas
class Figura(ABC):

    def __init__(self, cor, preenchimento=""):
        self.cor = cor
        self.preenchimento = preenchimento

    @abstractmethod
    def desenha(self, canvas, dash=()):
        pass

    @abstractmethod
    def vazia(self):
        pass
    
    @abstractmethod
    def contem(self, x, y) :
        pass

    @abstractmethod
    def mover(self, dx, dy) :
        pass

class PoliPontos(Figura, ABC) :
    
    def __init__(self, pontos=None, cor="black", preenchimento=""):
        super().__init__(cor, preenchimento)
        self.pontos = pontos if pontos is not None else []

    # Adiciona ponto se não está alinhado com os dois anteriores
    # Se alinhado, elimina o anterior
    def adiciona_ponto(self, x, y) :
        if len(self.pontos) >= 2 and\
           tres_pontos_alinhados(self.pontos[-2], self.pontos[-1], (x, y)) :
            self.pontos[-1] = (x,y)
        else :
            self.pontos.append((x,y))

    def mover(self, dx, dy) :
        for i in range(len(self.pontos)) :
            (x, y) = self.pontos[i]
            self.pontos[i] = (x+dx, y+dy)


            # Verifica se três pontos estão alinhados
def tres_pontos_alinhados(p1, p2, p3):
    """
    Checks if three 2D points are aligned in a straight line.
    Each point should be a tuple or list of (x, y).
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    # Calculate the cross product of vectors (p2-p1) and (p3-p2)
    # Formula: (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
    cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
    
    # Use a small tolerance for floating-point numbers
    return abs(cross_product) < 1e-12

#subclasse de figura que representa uma linha
class Linha(Figura):

    def __init__(self, x1, y1, x2, y2, cor="black", preenchimento=""):
        super().__init__(cor, preenchimento)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def desenha(self, canvas, dash=()):
        if not self.vazia():
            canvas.create_line(self.pontos, fill=self.cor, dash=dash)

    def vazia(self):
        return self.x1 == self.x2 and self.y1 == self.y2
    
    def contem(self, x , y) :
        return self.ini_x <= x <= self.fim_x and\
               self.ini_y <= y <= self.fim_y
    
    def mover(self, dx, dy) :
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

#subclasse de figura que representa um rabisco
class Rabisco(PoliPontos):

    def __init__(self, pontos=None, cor="black", preenchimento=""):
        super().__init__(pontos, cor, preenchimento)


    def desenha(self, canvas, dash=()):
        if len(self.pontos) >= 4:
            canvas.create_line(self.pontos, fill=self.cor, dash=dash)

    def vazia(self):
        return len(self.pontos) < 4
    
    # (px, py) está perto (<=epsilon) de self
    def contem(self, px, py) :
        epsilon = 3
        return any( distancia(x1, y1, x2, y2, px, py) <= epsilon
                    for (x1, y1), (x2, y2) in zip(self.pontos, self.pontos[1:])
                  )


#subclasse de figura que representa um retângulo
class Retangulo(Figura):

    def __init__(self,x1,y1,x2,y2,cor="black",preenchimento=""):
        super().__init__(cor,preenchimento)
        self.x1=x1; self.y1=y1; self.x2=x2; self.y2=y2

    def desenha(self,canvas,dash=()):
        canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,outline=self.cor,fill=self.preenchimento,dash=dash)

    def vazia(self):
        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)
        return largura < 3 or altura < 3
    
    def mover(self, dx, dy):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def contem(self, x, y):
        return (min(self.x1, self.x2) <= x <= max(self.x1, self.x2)
            and
            min(self.y1, self.y2) <= y <= max(self.y1, self.y2))

#subclasse de figura que representa um quadrado
class Quadrado(Retangulo):

    def __init__(self, x1, y1, x2, y2, cor="black", preenchimento=""):
        lado = min(abs(x2 - x1), abs(y2 - y1))

        if x2 < x1:
            x2 = x1 - lado
        else:
            x2 = x1 + lado

        if y2 < y1:
            y2 = y1 - lado
        else:
            y2 = y1 + lado

        super().__init__(x1, y1, x2, y2, cor, preenchimento)

#subclasse de figura que representa um oval
class Oval(Retangulo):
    def desenha(self,canvas,dash=()):
        canvas.create_oval(self.x1,self.y1,self.x2,self.y2,outline=self.cor,fill=self.preenchimento,dash=dash)
    def vazia(self) :
        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)
        return largura < 3 or altura < 3

#subclasse de figura que representa um círculo
class Circulo(Retangulo):
    def desenha(self,canvas,dash=()):
        r=min(abs(self.x2-self.x1),abs(self.y2-self.y1))
        canvas.create_oval(self.x1,self.y1,self.x1+r,self.y1+r,outline=self.cor,fill=self.preenchimento,dash=dash)

# distancia entre o segmento ((x1,y1), (x2,y2)) e o ponto (px, py)
def distancia(x1, y1, x2, y2, px, py) :
    # Vetor direção do segmento (AB)
    dx = x2 - x1
    dy = y2 - y1
    
    # Comprimento do segmento ao quadrado
    ab_len_sq = dx**2 + dy**2
    
    # Caso o segmento seja apenas um ponto (A e B são iguais)
    if ab_len_sq == 0:
        return math.sqrt((px - x1)**2 + (py - y1)**2)
    
    # Vetor do ponto A ao ponto P (AP)
    ap_x = px - x1
    ap_y = py - y1
    
    # Produto escalar de AP e AB dividido pelo comprimento ao quadrado (fator t)
    t = (ap_x * dx + ap_y * dy) / ab_len_sq
    
    # Limita t entre 0 e 1 para garantir que a projeção fique dentro do segmento
    t = max(0.0, min(1.0, t))
    
    # Coordenadas do ponto mais próximo no segmento
    ponto_proximo_x = x1 + t * dx
    ponto_proximo_y = y1 + t * dy 
    
    return math.sqrt((px - ponto_proximo_x)**2 + (py - ponto_proximo_y)**2)

