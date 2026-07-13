from dataclasses import dataclass
from tkinter import *
from view.janelaPaint import *
from model.figuras import *
from model.desenho import *
from controller.ferramenta import *

# ControladorPaint é a classe que representa o controlador do aplicativo de desenho
@dataclass
class ControladorPaint:
    visao : PaintView
    desenho : PaintModel    

    def __post_init__(self) :

        self.ferramentas = {"linha":Linha_ferramenta(self.visao, self.desenho),
                            "rabisco":Rabisco_ferramenta(self.visao, self.desenho),
                        "retangulo": Retangulo_ferramenta(self.visao, self.desenho),
                        "quadrado": Quadrado_ferramenta(self.visao, self.desenho),
                        "oval": Oval_ferramenta(self.visao, self.desenho),
                        "circulo": Circulo_ferramenta(self.visao, self.desenho),
}
        self.ferramenta_desenho = self.ferramentas['retangulo']
        self.visao.set_controller(self)

        # Para reagir quando o menu de ferramentas muda
        self.visao.fig_var.trace_add('write', self.muda_ferramenta)

        # Eventos do mouse para a área de desenho (canvas)
        canvas = self.visao.canvas
        canvas.bind("<ButtonPress-1>", self.mouse_pressionado)
        canvas.bind("<B1-Motion>", self.mouse_arrastado)
        canvas.bind("<ButtonRelease-1>", self.mouse_solto)

    # Ao mudar o option menu que escolhe a ferramenta de desenho
    def muda_ferramenta(self, *args) :
        figura = self.visao.fig_var.get()
        self.ferramenta_desenho = self.ferramentas[figura]
 
 ########### Eventos do mouse despachados para a ferramenta de desenho ##############
    
    #quando o mouse é pressionado, a posição inicial do desenho é armazenada
    def mouse_pressionado(self, event): 
        self.ferramenta_desenho.mouse_pressionado(event)

    #quando o mouse é arrastado, a figura é redesenhada no canvas
    def mouse_arrastado(self, event):
        self.ferramenta_desenho.mouse_arrastado(event)

    #quando o mouse é solto, a figura é adicionada à lista de figuras do modelo
    def mouse_solto(self, event): 
        self.ferramenta_desenho.mouse_solto(event)

    #muda a cor da borda da figura
    def mudar_cor(self, cor):

        self.desenho.mudar_cor(cor)

    #muda a cor de preenchimento da figura
    def mudar_preenchimento(self, cor):

        self.desenho.mudar_preenchimento(cor)

    # Salva o desenho em um arquivo
    def salvar(self, caminho):
        self.desenho.salvar(caminho)

    # Abre um desenho salvo
    def abrir(self, caminho):
        self.desenho.abrir(caminho)

        # redesenha o canvas
        self.desenho.desenha_figuras(self.visao.canvas)


