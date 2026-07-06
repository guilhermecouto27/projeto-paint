from dataclasses import dataclass, field

from model.figuras import Figura

@dataclass
class Retangulo(Figura) : # cria o retângulo

    x1: int
    y1: int
    x2: int
    y2: int
    cor:str="black"
    cor_preenchimento: str = ""

    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def desenha(self, canvas, preview=False):
        tag = "preview" if preview else ""
        canvas.create_rectangle(*self.pontos, tags=tag, outline=self.cor, fill=self.cor_preenchimento if self.cor_preenchimento else "")

    def atualizar(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def limpar(self):
        self.x1 = self.y1 = self.x2 = self.y2 = 0 # zeram as coordenadas 

    
    def vazia(self):
        altura = abs(self.x2 - self.x1)
        largura = abs(self.y2 - self.y1)

        return altura < 5 or largura < 5
    
# os métodos acabam se repetindo nas demais figuras