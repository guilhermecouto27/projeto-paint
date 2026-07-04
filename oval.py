from dataclasses import dataclass, field

from figuras import Figura
from tkinter import *

@dataclass
class Oval(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    cor:str="black"
    cor_preenchimento: str=""

    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def desenha(self, canvas, preview=False):
        tag = "preview" if preview else ""
        canvas.create_oval(*self.pontos, tags=tag, outline=self.cor, fill=self.cor_preenchimento if self.cor_preenchimento else "")

    def vazia(self):
        largura = abs(self.x2 - self.x1)
        altura = abs(self.y2 - self.y1)

        return largura < 5 or altura < 5

    def atualizar(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2