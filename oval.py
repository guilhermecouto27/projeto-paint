from dataclasses import dataclass

from figuras import Figura
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