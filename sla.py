from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

root = Tk()
root.title("Mini Paint Completo")

canvas = Canvas(root, bg="white", width=700, height=600)
canvas.pack()

# -------------------------
# ESTADO
# -------------------------
forma_atual = "retangulo"
cor_atual = "black"

x0 = y0 = None
figuras = []
figura_nova = None

# -------------------------
# UTIL
# -------------------------
def incompleta(figura):
    fig, v = figura

    if fig == "linha":
        return (v[0], v[1]) == (v[2], v[3])

    if fig == "rabisco":
        return len(v) <= 1

    return False

# -------------------------
# DESENHAR TUDO
# -------------------------
def desenhar():
    canvas.delete("all")

    for fig, v in figuras:

        if fig == "retangulo":
            canvas.create_rectangle(*v, fill=v[4], outline=v[4])

        elif fig == "oval":
            canvas.create_oval(*v, fill=v[4], outline=v[4])

        elif fig == "circulo":
            x, y, r, cor = v
            canvas.create_oval(x-r, y-r, x+r, y+r, fill=cor, outline=cor)

        elif fig == "linha":
            canvas.create_line(v[0], v[1], v[2], v[3], fill=v[4], width=2)

        elif fig == "rabisco":
            canvas.create_line(*v[1], fill=v[0], width=2)

# -------------------------
# PREVIEW
# -------------------------
def desenhar_preview():
    if figura_nova is None:
        return

    fig, v = figura_nova

    if fig == "linha":
        canvas.create_line(v[0], v[1], v[2], v[3], dash=(4, 2))

    elif fig == "rabisco":
        canvas.create_line(*v, dash=(4, 2))

    elif fig == "retangulo":
        canvas.create_rectangle(*v, outline=cor_atual, dash=(4, 2))

    elif fig == "oval":
        canvas.create_oval(*v, outline=cor_atual, dash=(4, 2))

    elif fig == "circulo":
        x, y, r = v
        canvas.create_oval(x-r, y-r, x+r, y+r, outline=cor_atual, dash=(4, 2))

# -------------------------
# MOUSE
# -------------------------
def press(event):
    global x0, y0, figura_nova

    x0, y0 = event.x, event.y

    if forma_atual == "rabisco":
        figura_nova = ("rabisco", [(x0, y0)])

    elif forma_atual == "linha":
        figura_nova = ("linha", (x0, y0, x0, y0))

    elif forma_atual == "circulo":
        figura_nova = ("circulo", (x0, y0, 0))

    else:
        figura_nova = (forma_atual, (x0, y0, x0, y0))

def move(event):
    global figura_nova

    if forma_atual == "rabisco":
        figura_nova[1].append((event.x, event.y))

    elif forma_atual == "linha":
        figura_nova = ("linha", (x0, y0, event.x, event.y))

    elif forma_atual == "circulo":
        r = ((event.x - x0)**2 + (event.y - y0)**2) ** 0.5
        figura_nova = ("circulo", (x0, y0, r))

    else:
        figura_nova = (forma_atual, (x0, y0, event.x, event.y))

    desenhar()
    desenhar_preview()

def release(event):
    global figura_nova

    if not incompleta(figura_nova):
        fig, v = figura_nova

        if fig == "retangulo":
            figuras.append(("retangulo", (*v, cor_atual)))

        elif fig == "oval":
            figuras.append(("oval", (*v, cor_atual)))

        elif fig == "circulo":
            x, y, r = v
            figuras.append(("circulo", (x, y, r, cor_atual)))

        elif fig == "linha":
            figuras.append(("linha", (*v, cor_atual)))

        elif fig == "rabisco":
            figuras.append(("rabisco", cor_atual, v))

    figura_nova = None
    desenhar()

# -------------------------
# CONTROLES
# -------------------------
def set_forma(f):
    global forma_atual
    forma_atual = f

def escolher_cor():
    global cor_atual
    cor = colorchooser.askcolor()[1]
    if cor:
        cor_atual = cor

def limpar():
    global figuras
    figuras = []
    desenhar()

# -------------------------
# BINDINGS
# -------------------------
canvas.bind("<ButtonPress-1>", press)
canvas.bind("<B1-Motion>", move)
canvas.bind("<ButtonRelease-1>", release)

# -------------------------
# MENU
# -------------------------
frame = Frame(root)
frame.pack()

tipo = ttk.Combobox(frame, values=[
    "retangulo", "oval", "circulo", "linha", "rabisco"
])
tipo.set("retangulo")
tipo.pack(side=LEFT)

def atualizar_forma(event):
    set_forma(tipo.get())

tipo.bind("<<ComboboxSelected>>", atualizar_forma)

Button(frame, text="Cor", command=escolher_cor).pack(side=LEFT)
Button(frame, text="Limpar", command=limpar).pack(side=LEFT)

root.mainloop()