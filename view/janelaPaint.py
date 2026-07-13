import tkinter as tk

#class PaintView é a classe que representa a interface gráfica do usuário (GUI) do aplicativo de desenho
class PaintView(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Paint da Mi e do Gui")

        self.controller = None

        self.canvas = tk.Canvas(
            self,
            bg="white",
            width=600,
            height=600
        )

        self.canvas.pack()

        self.fig_var = tk.StringVar(value="retangulo")

        self.criar_menu()

    def set_controller(self, controller):

        self.controller = controller

        self.canvas.bind("<Button-1>", self.controller.mouse_pressionado)
        self.canvas.bind("<B1-Motion>", self.controller.mouse_arrastado)
        self.canvas.bind("<ButtonRelease-1>", self.controller.mouse_solto)

    def desenhar(self, formas):

        self.canvas.delete("all")

        for forma in formas:
            forma.desenha(self.canvas)

    def criar_menu(self):

        menu = tk.Menu(self)

        self.config(menu=menu)

        # ---------------- FIGURAS ----------------

        mf = tk.Menu(menu, tearoff=0)

        menu.add_cascade(
            label="Selecionar figura",
            menu=mf
        )

        for lab, val in [

            ("Retângulo", "retangulo"),
            ("Círculo", "circulo"),
            ("Oval", "oval"),
            ("Linha", "linha"),
            ("Rabisco", "rabisco"),
            ("Quadrado","quadrado")]:

            mf.add_radiobutton( label=lab, variable=self.fig_var, value=val,)

        # ---------------- BORDA ----------------

        mb = tk.Menu(menu, tearoff=0)

        menu.add_cascade(label="Cor da borda", menu=mb)

        for nome, cor in [("Preto", "black"),
            ("Vermelho", "red"),
            ("Azul", "blue"),
            ("Verde", "green")]:

            mb.add_command(label=nome, command=lambda c=cor: self.controller.mudar_cor(c))

        # ---------------- PREENCHIMENTO ----------------

        mp = tk.Menu(menu, tearoff=0)

        menu.add_cascade(label="Preenchimento", menu=mp)

        mp.add_command(

            label="Sem preenchimento",

            command=lambda:
                self.controller.mudar_preenchimento(""))

        for nome, cor in [

            ("Preto", "black"),
            ("Vermelho", "red"),
            ("Azul", "blue"),
            ("Verde", "green")]:

            mp.add_command(label=nome, command=lambda c=cor:
                    self.controller.mudar_preenchimento(c))