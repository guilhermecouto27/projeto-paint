from dataclasses import dataclass

from figuras import Figura
@dataclass
class Rabisco(Figura):

    pontos: list
    cor: str="black"
    
    def desenha(self, canvas, preview=False, dash=()):
        tag = "preview" if preview else ""
        canvas.create_line(*self.pontos, tags=tag, dash=(5,5), fill=self.cor)# o rabisco sempre adiciona novas coordenadas

    def vazia(self):
        return len(self.pontos) <= 1
