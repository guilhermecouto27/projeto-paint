from dataclasses import dataclass, field
from figuras import Figura

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