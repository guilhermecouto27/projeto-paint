import tkinter as tk
from model.desenho import Desenhar
from model.figuras import Linha, Retangulo, Oval, Circulo, Rabisco
from view.janelaPaint import PaintView

class CriarPaint(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Paint da Mi e do Gui")

        self.formato_principal = "retangulo"

        self.x = None
        self.y = None
        self.fig = None

        # cor da borda
        self.cor_principal = "black"

        # cor do preenchimento
        self.cor_preenchimento = ""

        self.formas = []
        self.pontos_rabisco = []

        self.canvas = tk.Canvas(self, bg="white", width=600, height=600)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.inicio_mouse)
        self.canvas.bind("<B1-Motion>", self.movimento_mouse)
        self.canvas.bind("<ButtonRelease-1>", self.soltar_mouse)

        self.criar_menu()

    def inicio_mouse(self, event):

        if event.y < 0 :
            return 
        self.x = event.x
        self.y = event.y

        if self.formato_principal == "rabisco" :
            self.pontos_rabisco = [(self.x , self.y)]

    def movimento_mouse(self, event):

        if self.x is None or self.y is None :
            return 
        
        self.desenhar()

        if self.formato_principal ==  "rabisco" :
            self.pontos_rabisco.append((event.x, event.y))
            self.fig = Rabisco(self.pontos_rabisco, self.cor_principal)

        else:
            self.fig = self.criar_figura(self.x, self.y, event.x, event.y)

        if self.fig:
            self.fig.desenha(self.canvas, preview =True)

    def soltar_mouse(self, event):
        self.canvas.delete("preview")

        self.canvas.delete("temporario")

        if self.formato_principal == "rabisco" :
            self.pontos_rabisco.append((event.x, event.y))
            self.fig = Rabisco(self.pontos_rabisco, self.cor_principal)
            self.pontos_rabisco = []
        else:
            self.fig = self.criar_figura(self.x, self.y, event.x, event.y)

        if self.fig and not self.fig.vazia():
            self.formas.append(self.fig)

        self.desenhar()

    def criar_figura(self, x1, y1, x2, y2):
        if self.formato_principal == "linha":
            return Linha(x1, y1, x2, y2, self.cor_principal)
        elif self.formato_principal == "retangulo":
            return Retangulo(x1, y1, x2, y2, self.cor_principal, self.cor_preenchimento)
        elif self.formato_principal == "oval":
            return Oval(x1, y1, x2, y2, self.cor_principal, self.cor_preenchimento)
        elif self.formato_principal == "circulo":
            return Circulo(x1, y1, x2, y2, self.cor_principal, self.cor_preenchimento)
        return None

    def desenhar(self):
        self.canvas.delete("all")
        for forma in self.formas:
            forma.desenha(self.canvas, preview=False)

    def mudar_cor(self, cor):
        self.cor_principal = cor

    def mudar_preenchimento(self, cor):
        self.cor_preenchimento = cor

    def mudar_forma(self, forma):
        self.formato_principal = forma

    def criar_menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)

        self.fig_var = tk.StringVar(value=self.formato_principal)

        # -------- Selecionar figura --------
        mf = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Selecionar figura", menu=mf)

        for lab, val in [
            ("Retângulo", "retangulo"),
            ("Círculo", "circulo"),
            ("Oval", "oval"),
            ("Linha", "linha"),
            ("Rabisco", "rabisco")
        ]:
            mf.add_radiobutton(
                label=lab,
                variable=self.fig_var,
                value=val,
                command=lambda v=val: self.mudar_forma(v)
            )

        # -------- Cor da borda --------
        mb = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Cor da borda", menu=mb)

        for nome, cor in [
            ("Preto", "black"),
            ("Vermelho", "red"),
            ("Azul", "blue"),
            ("Verde", "green")
        ]:
            mb.add_command(
                label=nome,
                command=lambda c=cor: self.mudar_cor(c)
            )

        # -------- Preenchimento --------
        mp = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Preenchimento", menu=mp)

        mp.add_command(
            label="Sem preenchimento",
            command=lambda: self.mudar_preenchimento("")
        )

        for nome, cor in [
            ("Preto", "black"),
            ("Vermelho", "red"),
            ("Azul", "blue"),
            ("Verde", "green")
        ]:
            mp.add_command(
                label=nome,
                command=lambda c=cor: self.mudar_preenchimento(c)
            )



janela = CriarPaint()
janela.mainloop()