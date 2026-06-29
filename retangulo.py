from tkinter import *

#quando o mouse é pressionado
def inicia_retangulo(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y

#quando o mouse é movido com o botao pressionado
def atualiza_retangulo(event):
    desenhar()
    canvas.create_rectangle(ini_x, ini_y, event.x, event.y)

#quando o mouse é solto
def incluir_retangulo(event):
    retangulos.append((ini_x, ini_y, event.x, event.y))
    desenhar()

#desenha todos os retangulos salvos
def desenhar():
    canvas.delete("all")
    for retangulo in retangulos:
        x1, y1, x2, y2 = retangulo
        canvas.create_rectangle(x1, y1, x2, y2)


#******* MAIN *******#

# Todos os retângulos desenhados são armazenados aqui
retangulos = []

root = Tk()

canvas = Canvas(root, bg='white', width=600, height=600)
canvas.pack()

ini_x = None
ini_y = None

canvas.bind('<ButtonPress-1>', inicia_retangulo)
canvas.bind('<B1-Motion>', atualiza_retangulo)
canvas.bind('<ButtonRelease-1>', incluir_retangulo)

root.mainloop()

from tkinter import *

#quando o mouse é pressionado
def inicia_oval(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y

#quando o mouse é movido com o botao pressionado
def atualiza_oval(event):
    desenhar()
    canvas.create_oval(ini_x, ini_y, event.x, event.y)

#quando o mouse é solto
def incluir_oval(event):
    ovais.append((ini_x, ini_y, event.x, event.y))
    desenhar()

#desenha todos as formas ovais salvas
def desenhar():
    canvas.delete("all")
    for oval in ovais:
        x1, y1, x2, y2 = oval
        canvas.create_oval(x1, y1, x2, y2)


#******* MAIN *******#

# Todos os ovais desenhados são armazenados aqui
ovais = []

root2 = Tk()

canvas = Canvas(root2, bg='white', width=600, height=600)
canvas.pack()

ini_x = None
ini_y = None

canvas.bind('<ButtonPress-1>', inicia_oval)
canvas.bind('<B1-Motion>', atualiza_oval)
canvas.bind('<ButtonRelease-1>', incluir_oval)

root2.mainloop()