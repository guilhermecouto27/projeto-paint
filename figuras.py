from abc import ABC, abstractmethod

from dataclasses import dataclass, field
#criando a classe principal FIGURA para que os mesmos métodos dela sejam utilizados nas outras classes(que também são figuras)
class Figura(ABC):
    @abstractmethod
    def desenha(self, canvas, preview=False):
        pass

    @abstractmethod
    def vazia(self):
        return False # as figuras precisam desenhar e identificar quando estão vazias


@dataclass 
class Linha(Figura):
    x1: int
    y1: int # como o construtor já foi aplicado, basta apenas atribuir os tipos ás coordenadas
    x2: int
    y2: int
    cor: str="black"

    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2) # o método pode ser atribuído

    def atualizar(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2  # coordenadas antigas atualizam
        self.y2 = y2

    def desenha(self, canvas, preview=False):
        tag = "preview" if preview else ""
        canvas.create_line(*self.pontos, tags=tag, fill=self.cor)

        # verifica se o desenha é uma prévia ou não através da tag. isso impede que o senho seja feito várias vezes

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2) # a própria classe entende que está vazia com essas condições


@dataclass
class Rabisco(Figura):

    pontos: list
    cor: str="black"
    
    def desenha(self, canvas, preview=False, dash=()):
        tag = "preview" if preview else ""
        canvas.create_line(*self.pontos, tags=tag, dash=(5,5), fill=self.cor)# o rabisco sempre adiciona novas coordenadas

    def vazia(self):
        return len(self.pontos) <= 1

@dataclass
class Retangulo(Figura) : # cria o retângulo

    x1: int
    y1: int
    x2: int
    y2: int
    cor:str="black"

    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def desenha(self, canvas, preview=False):
        tag = "preview" if preview else ""
        canvas.create_rectangle(*self.pontos, tags=tag, outline=self.cor)

    def atualizar(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def limpar(self):
        self.x1 = self.y1 = self.x2 = self.y2 = 0 # zeram as coordenadas 

    
    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)
    
# os métodos acabam se repetindo nas demais figuras

@dataclass
class Circulo(Figura) : # cria o círculo

    x1: int
    y1: int
    x2: int
    y2: int
    cor: str="black"

    @property
    def pontos(self):
        raio = min(abs(self.x2 - self.x1), abs(self.y2 - self.y1))
        x_final = self.x1 + raio if self.x2 >= self.x1 else self.x1 - raio # sempre calculando a menor distância para que a largura e altura sejam as mesmas
        y_final = self.y1 + raio if self.y2 >= self.y1 else self.y1 - raio
        return (self.x1, self.y1, x_final, y_final)
    
    def desenha(self, canvas, preview=False):
        tag = "preview" if preview else ""
        canvas.create_oval(*self.pontos, tags=tag, outline = self.cor)

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)
    
    def atualizar(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def limpar(self):
        self.x1 = self.y1 = self.x2 = self.y2 = 0
    
@dataclass
class Oval(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    cor:str="black"

    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def desenha(self, canvas, preview=False):
        tag = "preview" if preview else ""
        canvas.create_oval(*self.pontos, tags=tag, outline=self.cor)

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2) 

    def atualizar(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
