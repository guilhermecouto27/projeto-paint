from figuras import Figura
from dataclasses import dataclass, field

@dataclass
class Circulo(Figura) : # cria o círculo

    x1: int
    y1: int
    x2: int
    y2: int
    cor: str="black"
    cor_preenchimento: str=""

    @property
    def pontos(self):
        raio = min(abs(self.x2 - self.x1), abs(self.y2 - self.y1))
        x_final = self.x1 + raio if self.x2 >= self.x1 else self.x1 - raio # sempre calculando a menor distância para que a largura e altura sejam as mesmas
        y_final = self.y1 + raio if self.y2 >= self.y1 else self.y1 - raio
        return (self.x1, self.y1, x_final, y_final)
    
    def desenha(self, canvas, preview=False):
        tag = "preview" if preview else ""
        canvas.create_oval(*self.pontos, tags=tag, outline = self.cor, fill=self.cor_preenchimento if self.cor_preenchimento else "")

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)
    
    def atualizar(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def limpar(self):
        self.x1 = self.y1 = self.x2 = self.y2 = 0
    