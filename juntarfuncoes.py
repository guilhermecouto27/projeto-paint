from tkinter import *

# receber do usuário

formato_principal = "retangulo"
cor_borda = "black"
cor_preenchimento = ""

fig = None

#quando o mouse é pressionado, armazenar a posição inicial
def iniciar_mouse(event):
    global ini_x, ini_y
    ini_x, ini_y = event.x, event.y
    atualizar.x_antigo = event.x
    atualizar.y_antigo = event.y

#quando o mouse é arrastado, atualizar a figura
def atualizar(event):
    global fig
    if formato_principal != "rabisco" and fig:
        canvas.delete(fig)

    if formato_principal == "retangulo":
        fig = canvas.create_rectangle(ini_x, ini_y, event.x, event.y,
                                      outline=cor_borda, fill=cor_preenchimento)
    elif formato_principal == "oval":
        fig = canvas.create_oval(ini_x, ini_y, event.x, event.y,
                                 outline=cor_borda, fill=cor_preenchimento)
    elif formato_principal == "circulo":
        raio = min(abs(event.x-ini_x), abs(event.y-ini_y))
        xf = ini_x + raio if event.x >= ini_x else ini_x - raio
        yf = ini_y + raio if event.y >= ini_y else ini_y - raio
        fig = canvas.create_oval(ini_x, ini_y, xf, yf,
                                 outline=cor_borda, fill=cor_preenchimento)
    elif formato_principal == "linha":
        fig = canvas.create_line(ini_x, ini_y, event.x, event.y,
                                 fill=cor_borda, width=3)
    elif formato_principal == "rabisco":
        canvas.create_line(atualizar.x_antigo, atualizar.y_antigo,
                           event.x, event.y, fill=cor_borda, width=3)
        atualizar.x_antigo, atualizar.y_antigo = event.x, event.y

#quando o mouse é solto, finalizar a figura
def soltar_mouse(event):
    global fig
    fig = None

#funções para mudar o formato e as cores
def mudar_fig(*args):
    global formato_principal
    formato_principal = fig_var.get()

#função para mudar a cor da borda
def mudar_cor_borda(cor):
    global cor_borda
    cor_borda = cor

#função para mudar a cor de preenchimento
def mudar_cor_preenchimento(cor):
    global cor_preenchimento
    cor_preenchimento = cor

#*********MAIN*********
janela = Tk()
janela.title("Paint da Mi e do Gui")
Label(janela,text=".✦ ݁˖Paint da Mi e do Gui.✦ ݁˖",font=("Times New Roman",20)).pack()
canvas = Canvas(janela,bg="white",width=800,height=800)
canvas.pack()

menu=Menu(janela); janela.config(menu=menu)

fig_var=StringVar(value="retangulo")
fig_var.trace_add("write",mudar_fig)

mf=Menu(menu,tearoff=0)
menu.add_cascade(label="Selecionar figura",menu=mf)
for lab,val in [("Retângulo","retangulo"),("Círculo","circulo"),("Oval","oval"),("Linha","linha"),("Rabisco","rabisco")]:
    mf.add_radiobutton(label=lab,variable=fig_var,value=val)

mb=Menu(menu,tearoff=0)
menu.add_cascade(label="Cor da borda",menu=mb)
for nome,cor in [("Preto","black"),("Vermelho","red"),("Azul","blue"),("Verde","green")]:
    mb.add_command(label=nome,command=lambda c=cor:mudar_cor_borda(c))

mp=Menu(menu,tearoff=0)
menu.add_cascade(label="Preenchimento",menu=mp)
mp.add_command(label="Sem preenchimento",command=lambda:mudar_cor_preenchimento(""))
for nome,cor in [("Preto","black"),("Vermelho","red"),("Azul","blue"),("Verde","green")]:
    mp.add_command(label=nome,command=lambda c=cor:mudar_cor_preenchimento(c))

# permite que o usuário clique em UMA das opções e as funções responsáveis por cada figura sejam chamadas e executadas
canvas.bind("<Button-1>",iniciar_mouse)
canvas.bind("<B1-Motion>",atualizar)
canvas.bind("<ButtonRelease-1>",soltar_mouse)

janela.mainloop()
