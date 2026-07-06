from dataclasses import dataclass, field


from model.figuras import Figura

@dataclass
class Rabisco(Figura):

    pontos: list = field(default_factory=list)
    cor: str="black"
    
    def desenha(self, canvas, preview=False, dash=()):
        if len(self.pontos) < 2:
            return
        
        coordenadas = [coord for ponto in self.pontos for coord in ponto]
        tag = "preview" if preview else ""
        canvas.create_line(coordenadas, tags=tag, dash=(5,5), fill=self.cor)# o rabisco sempre adiciona novas coordenadas


    def vazia(self):
        return len(self.pontos) <= 1
