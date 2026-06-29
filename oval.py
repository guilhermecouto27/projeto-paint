from tkinter import *

root = Tk()

#quando o mouse é pressionado
def inicia_oval(event):
    global ini2_x, ini2_y
    ini2_x = event.x
    ini2_y = event.y

#quando o mouse é movido com o botao pressionado
def atualiza_oval(event):
    desenhar_ovais()
    canvas2.create_oval(ini2_x, ini2_y, event.x, event.y)

#quando o mouse é solto
def incluir_oval(event):
    ovais.append((ini2_x, ini2_y, event.x, event.y))
    desenhar_ovais()

#desenha todos as formas ovais salvas
def desenhar_ovais():
    canvas2.delete("all")
    for oval in ovais:
        x1, y1, x2, y2 = oval
        canvas2.create_oval(x1, y1, x2, y2)


#******* MAIN *******#

# Todos os ovais desenhados são armazenados aqui
ovais = []

canvas2 = Canvas(root, bg='white', width=600, height=600)
canvas2.pack()

ini2_x = None
ini2_y = None

canvas2.bind('<ButtonPress-1>', inicia_oval)
canvas2.bind('<B1-Motion>', atualiza_oval)
canvas2.bind('<ButtonRelease-1>', incluir_oval)

root.mainloop()