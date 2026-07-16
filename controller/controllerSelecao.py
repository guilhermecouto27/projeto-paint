from dataclasses import dataclass
from view.janelaPaint import PaintView
from model.desenho import PaintModel

@dataclass
class ControladorSelecao : 
    visao : PaintView
    desenho : PaintModel
    
    def selecionar(self, x, y):
        self.desenho.seleciona(x, y)
        self.desenho.desenha_figuras(self.visao.canvas)