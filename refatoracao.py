from abc import ABC, abstractmethod
from dataclasses import dataclass

class Figura(ABC):
    @abstractmethod
    def desenha(self, canvas, dash=()):
        pass

    @abstractmethod
    def vazia(self):
        return False


@dataclass
class Linha(Figura):
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def desenha(self, canvas, dash=()):
        canvas.create_line(self.pontos, dash=dash)

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)


@dataclass
class Rabisco(Figura):
    pontos: list

    def desenha(self, canvas, dash=(5,5)):
        canvas.create_line(self.pontos, dash=dash)

    def vazia(self):
        return len(self.pontos) <= 1


@dataclass
class Retangulo(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    cor: str = "black"

    def desenha(self, canvas, dash=()):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor, dash=dash)

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)


@dataclass
class Oval(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    cor: str = "black"

    def desenha(self, canvas, dash=()):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline=self.cor, dash=dash)

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)


@dataclass
class Circulo(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    cor: str = "black"

    def desenha(self, canvas, dash=()):
        # círculo perfeito: ajusta largura e altura
        r = min(abs(self.x2 - self.x1), abs(self.y2 - self.y1))
        canvas.create_oval(self.x1, self.y1, self.x1 + r, self.y1 + r, outline=self.cor, dash=dash)

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)


import tkinter as tk

class CriarPaint(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Paint da Mi e do Gui")

        self.x = None
        self.y = None
        self.fig = None

        self.formato_principal = "retangulo"
        self.cor_principal = "black"
        self.formas = []

        self.canvas = tk.Canvas(self, bg="white", width=600, height=600)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.inicio_mouse)
        self.canvas.bind("<B1-Motion>", self.movimento_mouse)
        self.canvas.bind("<ButtonRelease-1>", self.soltar_mouse)

        self.criar_menu()

    def inicio_mouse(self, event):
        self.x, self.y = event.x, event.y

    def movimento_mouse(self, event):
        self.desenhar()
        self.fig = self.criar_figura(self.x, self.y, event.x, event.y)
        if self.fig:
            self.fig.desenha(self.canvas)

    def soltar_mouse(self, event):
        self.fig = self.criar_figura(self.x, self.y, event.x, event.y)
        if self.fig and not self.fig.vazia():
            self.formas.append(self.fig)
        self.desenhar()

    def criar_figura(self, x1, y1, x2, y2):
        if self.formato_principal == "linha":
            return Linha(x1, y1, x2, y2)
        elif self.formato_principal == "rabisco":
            return Rabisco([(x1, y1), (x2, y2)])
        elif self.formato_principal == "retangulo":
            return Retangulo(x1, y1, x2, y2, self.cor_principal)
        elif self.formato_principal == "oval":
            return Oval(x1, y1, x2, y2, self.cor_principal)
        elif self.formato_principal == "circulo":
            return Circulo(x1, y1, x2, y2, self.cor_principal)
        return None

    def desenhar(self):
        self.canvas.delete("all")
        for forma in self.formas:
            forma.desenha(self.canvas)

    def mudar_cor(self, cor):
        self.cor_principal = cor

    def mudar_forma(self, forma):
        self.formato_principal = forma

    def criar_menu(self):
        frame = tk.Frame(self)
        frame.pack()

        # menu de cores
        for cor in ["black", "red", "blue", "green"]:
            tk.Button(frame, text=cor.capitalize(), bg=cor,
                      fg="white" if cor in ["black", "blue"] else "black",
                      command=lambda c=cor: self.mudar_cor(c)).pack(side="left")

        # menu de formas
        for forma in ["linha", "rabisco", "retangulo", "oval", "circulo"]:
            tk.Button(frame, text=forma.capitalize(),
                      command=lambda f=forma: self.mudar_forma(f)).pack(side="left")


# -------- MAIN --------
if __name__ == "__main__":
    app = CriarPaint()
    app.mainloop()