from dataclasses import dataclass

from figuras import Figura
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