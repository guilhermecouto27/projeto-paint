from model.figuras import Linha, Rabisco, Retangulo, Quadrado, Oval, Circulo


class PaintController:

    def __init__(self, model, view):

        self.model = model
        self.view = view

        self.view.set_controller(self)

    def inicio_mouse(self, event):

        if event.y < 0:
            return

        self.model.x = event.x
        self.model.y = event.y

        if self.model.formato_principal == "rabisco":
            self.model.pontos_rabisco = [(event.x, event.y)]

    def movimento_mouse(self, event):

        if self.model.x is None or self.model.y is None:
            return

        # redesenha tudo que já existe
        self.view.desenhar(self.model.formas)

        if self.model.formato_principal == "rabisco":

            self.model.pontos_rabisco.append((event.x, event.y))

            self.model.fig = Rabisco(self.model.pontos_rabisco, self.model.cor_principal)

        else:

            self.model.fig = self.criar_figura(self.model.x, self.model.y, event.x, event.y)

        if self.model.fig:
            self.model.fig.desenha(self.view.canvas)

    def soltar_mouse(self, event):

        if self.model.formato_principal == "rabisco":

            self.model.pontos_rabisco.append((event.x, event.y))

            self.model.fig = Rabisco(self.model.pontos_rabisco, self.model.cor_principal)

            self.model.pontos_rabisco = []

        else:

            self.model.fig = self.criar_figura(self.model.x, self.model.y, event.x, event.y)

        if self.model.fig and not self.model.fig.vazia():

            self.model.formas.append(self.model.fig)

        self.view.desenhar(self.model.formas)

        self.model.x = None
        self.model.y = None
    
    def criar_figura(self, x1, y1, x2, y2):

        if self.model.formato_principal == "linha":

            return Linha(x1, y1, x2, y2, self.model.cor_principal)

        elif self.model.formato_principal == "rabisco":

            return Rabisco(self.model.pontos_rabisco, self.model.cor_principal)

        elif self.model.formato_principal == "retangulo":

            return Retangulo(x1, y1,  x2, y2, self.model.cor_principal, self.model.cor_preenchimento)
        
        elif self.model.formato_principal == "quadrado":

            return Quadrado(x1, y1, x2, y2, self.model.cor_principal,self.model.cor_preenchimento)

        elif self.model.formato_principal == "oval":

            return Oval(x1, y1, x2, y2, self.model.cor_principal, self.model.cor_preenchimento)

        elif self.model.formato_principal == "circulo":

            return Circulo(x1, y1, x2, y2, self.model.cor_principal, self.model.cor_preenchimento)

        return None

    def mudar_cor(self, cor):

        self.model.mudar_cor(cor)

    def mudar_preenchimento(self, cor):

        self.model.mudar_preenchimento(cor)

    def mudar_forma(self, forma):

        self.model.mudar_forma(forma)