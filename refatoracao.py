from abc import ABC, abstractmethod
from dataclasses import dataclass
<<<<<<< HEAD
import tkinter as tk

=======
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48

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
<<<<<<< HEAD
    cor: str = "black"
=======
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48

    @property
    def pontos(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def desenha(self, canvas, dash=()):
<<<<<<< HEAD
        canvas.create_line(self.pontos, fill=self.cor, dash=dash)
=======
        canvas.create_line(self.pontos, dash=dash)
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)


@dataclass
class Rabisco(Figura):
    pontos: list
<<<<<<< HEAD
    cor: str = "black"

    def desenha(self, canvas, dash=(5, 5)):
        canvas.create_line(self.pontos, fill=self.cor, dash=dash)
=======

    def desenha(self, canvas, dash=(5,5)):
        canvas.create_line(self.pontos, dash=dash)
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48

    def vazia(self):
        return len(self.pontos) <= 1


@dataclass
class Retangulo(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    cor: str = "black"
<<<<<<< HEAD
    preenchimento: str = ""

    def desenha(self, canvas, dash=()):
        canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2,
            outline=self.cor,
            fill=self.preenchimento,
            dash=dash
        )
=======

    def desenha(self, canvas, dash=()):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor, dash=dash)
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)


@dataclass
class Oval(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    cor: str = "black"
<<<<<<< HEAD
    preenchimento: str = ""

    def desenha(self, canvas, dash=()):
        canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2,
            outline=self.cor,
            fill=self.preenchimento,
            dash=dash
        )
=======

    def desenha(self, canvas, dash=()):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline=self.cor, dash=dash)
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)


@dataclass
class Circulo(Figura):
    x1: int
    y1: int
    x2: int
    y2: int
    cor: str = "black"
<<<<<<< HEAD
    preenchimento: str = ""

    def desenha(self, canvas, dash=()):
        r = min(abs(self.x2 - self.x1), abs(self.y2 - self.y1))
        canvas.create_oval(
            self.x1,
            self.y1,
            self.x1 + r,
            self.y1 + r,
            outline=self.cor,
            fill=self.preenchimento,
            dash=dash
        )
=======

    def desenha(self, canvas, dash=()):
        # círculo perfeito: ajusta largura e altura
        r = min(abs(self.x2 - self.x1), abs(self.y2 - self.y1))
        canvas.create_oval(self.x1, self.y1, self.x1 + r, self.y1 + r, outline=self.cor, dash=dash)
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48

    def vazia(self):
        return (self.x1, self.y1) == (self.x2, self.y2)


<<<<<<< HEAD
class CriarPaint(tk.Tk):
    def __init__(self):
        super().__init__()

=======
import tkinter as tk

class CriarPaint(tk.Tk):
    def __init__(self):
        super().__init__()
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48
        self.title("Paint da Mi e do Gui")

        self.x = None
        self.y = None
        self.fig = None

        self.formato_principal = "retangulo"
<<<<<<< HEAD

        # cor da borda
        self.cor_principal = "black"

        # cor do preenchimento
        self.cor_preenchimento = ""

=======
        self.cor_principal = "black"
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48
        self.formas = []

        self.canvas = tk.Canvas(self, bg="white", width=600, height=600)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.inicio_mouse)
        self.canvas.bind("<B1-Motion>", self.movimento_mouse)
        self.canvas.bind("<ButtonRelease-1>", self.soltar_mouse)

        self.criar_menu()

    def inicio_mouse(self, event):
<<<<<<< HEAD
        self.x = event.x
        self.y = event.y
=======
        self.x, self.y = event.x, event.y
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48

    def movimento_mouse(self, event):
        self.desenhar()
        self.fig = self.criar_figura(self.x, self.y, event.x, event.y)
<<<<<<< HEAD

=======
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48
        if self.fig:
            self.fig.desenha(self.canvas)

    def soltar_mouse(self, event):
        self.fig = self.criar_figura(self.x, self.y, event.x, event.y)
<<<<<<< HEAD

        if self.fig and not self.fig.vazia():
            self.formas.append(self.fig)

=======
        if self.fig and not self.fig.vazia():
            self.formas.append(self.fig)
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48
        self.desenhar()

    def criar_figura(self, x1, y1, x2, y2):
        if self.formato_principal == "linha":
<<<<<<< HEAD
            return Linha(x1, y1, x2, y2, self.cor_principal)
        elif self.formato_principal == "rabisco":
            return Rabisco([(x1, y1), (x2, y2)], self.cor_principal)
        elif self.formato_principal == "retangulo":
            return Retangulo(x1, y1, x2, y2, self.cor_principal, self.cor_preenchimento)
        elif self.formato_principal == "oval":
            return Oval(x1, y1, x2, y2, self.cor_principal, self.cor_preenchimento)
        elif self.formato_principal == "circulo":
            return Circulo(x1, y1, x2, y2, self.cor_principal, self.cor_preenchimento)
=======
            return Linha(x1, y1, x2, y2)
        elif self.formato_principal == "rabisco":
            return Rabisco([(x1, y1), (x2, y2)])
        elif self.formato_principal == "retangulo":
            return Retangulo(x1, y1, x2, y2, self.cor_principal)
        elif self.formato_principal == "oval":
            return Oval(x1, y1, x2, y2, self.cor_principal)
        elif self.formato_principal == "circulo":
            return Circulo(x1, y1, x2, y2, self.cor_principal)
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48
        return None

    def desenhar(self):
        self.canvas.delete("all")
        for forma in self.formas:
            forma.desenha(self.canvas)

    def mudar_cor(self, cor):
        self.cor_principal = cor

<<<<<<< HEAD
    def mudar_preenchimento(self, cor):
        self.cor_preenchimento = cor

=======
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48
    def mudar_forma(self, forma):
        self.formato_principal = forma

    def criar_menu(self):
<<<<<<< HEAD
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


=======
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
>>>>>>> 4e86e459016aa8ab2016d5aef2de3b7ae1b6da48
if __name__ == "__main__":
    app = CriarPaint()
    app.mainloop()