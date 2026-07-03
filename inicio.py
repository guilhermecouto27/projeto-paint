import tkinter as tk
from classefiguras import Linha, Rabisco, Circulo, Retangulo, Oval

class criar_paint(tk.Tk) :

    def __init__(self) :
        super().__init__()  # permite que a janela seja criada

        self.x = None
        self.y = None
        self.fig = None # informações do usuário, como: coordenadas clicadas e figuras escolhidas

        self.formato_principal ="oval" # cores escolhidas pelo usuário
        self.cor_principal = "red"

        self.canvas = tk.Canvas(self, bg = "white" , width=600 , height=600) # cria o local do desenho
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.inicio_mouse)  # identifica os movimentos feitos pelo usuário e qual movimento determina a função
        self.canvas.bind("<B1-Motion>" , self.movimento_mouse)
        self.canvas.bind("<ButtonRelease-1>", self.soltar_mouse)

    def inicio_mouse(self,event) :

        self.x = event.x
        self.y = event.y
        # define a figura a ser criada e as posições iniciais 

        if self.formato_principal == "rabisco":
            self.fig = Rabisco([event.x, event.y], self.cor_principal) # primeiro ponto do rabisco

        elif self.formato_principal == "linha":
            self.fig = Linha(self.x, self.y, event.x, event.y, self.cor_principal)

        elif self.formato_principal == "retangulo":
            self.fig = Retangulo(self.x , self.y , event.x, event.y,self.cor_principal)
    
        elif self.formato_principal == "circulo":
            self.fig = Circulo(self.x, self.y, event.x, event.y, self.cor_principal)

        else:
            self.fig = Oval(self.x, self.y, event.x, event.y, self.cor_principal)

        

        self.fig.desenha(self.canvas)

    def movimento_mouse(self, event):

        self.canvas.delete("preview")

        if self.formato_principal == "rabisco":
            self.fig.pontos.extend([event.x, event.y]) # adiciona novos pontos
        else:
            self.fig.atualizar(self.x, self.y, event.x, event.y) # muda coordenadas

        self.fig.desenha(self.canvas, preview=True) # desenha o pré desenho para que depois seja apagado e não desenhado várias vezes 

        
    def soltar_mouse(self, event):

        self.canvas.delete("preview") 
        if self.fig:
            self.fig.desenha(self.canvas) # aplica a figura de fato

        self.fig = None

    def cores(self, cor) :
        self.cor_principal = cor # muda a cor da figura de acordo com o usuário
    
janela = criar_paint() # cria a janela 
janela.mainloop()
