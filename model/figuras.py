from abc import ABC, abstractmethod

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

#subclasse de figura que representa um rabisco
class Rabisco(Figura):

    def __init__(self, pontos=None, cor="black", preenchimento=""):
        super().__init__(cor, preenchimento)
        self.pontos = pontos if pontos else []

    def desenha(self, canvas, dash=()):
        if len(self.pontos) >= 4:
            canvas.create_line(self.pontos, fill=self.cor, dash=dash)

    def vazia(self):
        return len(self.pontos) < 4

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
