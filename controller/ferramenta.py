from dataclasses import dataclass
from abc import ABC, abstractmethod
from tkinter import *
from view.janelaPaint import PaintView
from model.figuras import Linha, Oval, Circulo, Quadrado, Retangulo, Rabisco
from model.desenho import PaintModel

@dataclass
class Ferramenta(ABC) :
    visao : PaintView
    desenho : PaintModel

    def __post_init__(self) :
        self.canvas = self.visao.canvas

    @abstractmethod
    def mouse_pressionado(self, event) :
        pass

    @abstractmethod
    def mouse_arrastado(self, event) :
        pass

    @abstractmethod
    def mouse_solto(self, event) :
        pass

# --------LINHA-----------
@dataclass
class Linha_ferramenta(Ferramenta) :
    linha_nova : Linha = None

    def mouse_pressionado(self, event):
        self.linha_nova = Linha(event.x, event.y, event.x, event.y)

    def mouse_arrastado(self, event):
        self.linha_nova = Linha(self.linha_nova.x1, self.linha_nova.y1, event.x, event.y, self.desenho.cor_principal)
        self.desenho.desenha_figuras(self.canvas)
        self.linha_nova.desenha(self.canvas, dash= (4,2))

    def mouse_solto(self,event) :
        if not self.linha_nova.vazia() :
            self.desenho.adiciona_figura(self.linha_nova)
        self.desenho.desenha_figuras(self.canvas)

# ----------- RABISCO ----------------
@dataclass
class Rabisco_ferramenta(Ferramenta) :
    rabisco_atual : Rabisco = None

    def mouse_pressionado(self, event):
        self.rabisco_atual = Rabisco([(event.x, event.y)], self.desenho.cor_principal)
    
    def mouse_arrastado(self, event):
        self.rabisco_atual.pontos.append((event.x, event.y)) 
        self.desenho.desenha_figuras(self.canvas)
        self.rabisco_atual.desenha(self.canvas, dash=(4, 2))

    def mouse_solto(self, event):
        self.rabisco_atual.pontos.append((event.x, event.y))
        if not self.rabisco_atual.vazia() :
            self.desenho.adiciona_figura(self.rabisco_atual)
        self.desenho.desenha_figuras(self.canvas)

        self.rabisco_atual = None

#-------------OVAL-------------
@dataclass
class Oval_ferramenta(Ferramenta) :
    oval_atual : Oval = None

    def mouse_pressionado(self, event):
        self.oval_atual = Oval(event.x, event.y, event.x, event.y, self.desenho.cor_principal, self.desenho.cor_preenchimento)
    
    def mouse_arrastado(self, event):
        self.oval_atual = Oval(self.oval_atual.x1, self.oval_atual.y1, event.x, event.y, self.desenho.cor_principal, self.desenho.cor_preenchimento)
        self.desenho.desenha_figuras(self.canvas)
        self.oval_atual.desenha(self.canvas, dash=(4,4))

    def mouse_solto(self,event) :
        if not self.oval_atual.vazia() :
            self.desenho.adiciona_figura(self.oval_atual)
        self.desenho.desenha_figuras(self.canvas)

#------------RETÂNGULO-------------
@dataclass
class Retangulo_ferramenta(Ferramenta) :
    retangulo_atual : Retangulo = None

    def mouse_pressionado(self, event):
        self.retangulo_atual = Retangulo(event.x, event.y, event.x, event.y, )

    def mouse_arrastado(self, event):
        self.retangulo_atual = Retangulo(self.retangulo_atual.x1, self.retangulo_atual.y1, event.x , event.y ,self.desenho.cor_principal, self.desenho.cor_preenchimento)
        self.desenho.desenha_figuras(self.canvas)
        self.retangulo_atual.desenha(self.canvas, dash= (4,2))

    def mouse_solto(self,event) :
        if not self.retangulo_atual.vazia() :
            self.desenho.adiciona_figura(self.retangulo_atual)
        self.desenho.desenha_figuras(self.canvas)

#------------CÍRCULO--------------
@dataclass
class Circulo_ferramenta(Ferramenta) :
    circulo_atual : Circulo = None

    def mouse_pressionado(self, event):
        self.circulo_atual = Circulo(event.x, event.y, event.x, event.y, self.desenho.cor_principal, self.desenho.cor_preenchimento)

    def mouse_arrastado(self, event):
        self.circulo_atual =  Circulo(self.circulo_atual.x1, self.circulo_atual.y1, event.x, event.y , self.desenho.cor_principal, self.desenho.cor_preenchimento)
        self.desenho.desenha_figuras(self.canvas)
        self.circulo_atual.desenha(self.canvas, dash= (4,2))

    def mouse_solto(self,event) :
        if not self.circulo_atual.vazia() :
            self.desenho.adiciona_figura(self.circulo_atual)
        self.desenho.desenha_figuras(self.canvas)

#----------QUADRADO---------------
@dataclass
class Quadrado_ferramenta(Ferramenta) :
    quadrado_atual : Quadrado = None

    def mouse_pressionado(self, event):
        self.quadrado_atual = Quadrado(event.x, event.y, event.x, event.y, self.desenho.cor_principal, self.desenho.cor_preenchimento)

    def mouse_arrastado(self, event):
        self.quadrado_atual = Quadrado(self.quadrado_atual.x1, self.quadrado_atual.y1, event.x, event.y, self.desenho.cor_principal, self.desenho.cor_preenchimento)
        self.desenho.desenha_figuras(self.canvas)
        self.quadrado_atual.desenha(self.canvas, dash= (4,2))

    def mouse_solto(self,event) :
        if not self.quadrado_atual.vazia() :
            self.desenho.adiciona_figura(self.quadrado_atual)
        self.desenho.desenha_figuras(self.canvas)       
    