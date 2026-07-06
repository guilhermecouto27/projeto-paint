import tkinter as tk

janela = tk.Tk()
janela.title("Mini Paint")

#cor base
cor_atual = "black"

canvas = tk.Canvas(janela, bg="white", width=600, height=400)
canvas.pack()

# funcao para mudar a cor do retangulo
def mudar_cor(cor):
    global cor_atual
    cor_atual = cor

#quando o mouse é pressionado
def inicia_retangulo(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y

# Quando o mouse é movido com o botão pressionado
def atualiza_retangulo(event):
    canvas.create_rectangle(
        ini_x, ini_y,
        event.x, event.y,
        outline=cor_atual
    )

# Quando o mouse é solto
def incluir_retangulo(event):
    retangulos.append((ini_x, ini_y, event.x, event.y, cor_atual))


#******* MAIN *******#

# Todos os retângulos desenhados são armazenados aqui
retangulos = []

canvas.bind("<Button-1>", inicia_retangulo)
canvas.bind("<B1-Motion>", atualiza_retangulo)
canvas.bind("<ButtonRelease-1>", incluir_retangulo)

frame = tk.Frame(janela)
frame.pack()

#menu das cores
tk.Button(frame, text="Preto",
          bg="black", fg="white",
          command=lambda: mudar_cor("black")).pack(side="left")

tk.Button(frame, text="Vermelho",
          bg="red",
          command=lambda: mudar_cor("red")).pack(side="left")

tk.Button(frame, text="Azul",
          bg="blue", fg="white",
          command=lambda: mudar_cor("blue")).pack(side="left")

tk.Button(frame, text="Verde",
          bg="green",
          command=lambda: mudar_cor("green")).pack(side="left")

janela.mainloop()