from tkinter import *

# receber do usuário 

formato_principal = "retangulo" # formato e cores padrões até o usuário escolher mudar
cor_principal = "black"

x_inicial = None
y_inicial = None
fig = None

#mouse sendo pressionado
def iniciar_mouse(event) :
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y

    atualizar.x_antigo = event.x
    atualizar.y_antigo = event.y

def atualizar(event) :
    global fig

    if formato_principal != "rabisco" :
        if fig :
            canvas.delete(fig) #responsável por desenhar uma figura nova diferente do rabisco
    
    if formato_principal == "retangulo" :
        fig = canvas.create_rectangle(ini_x, ini_y , event.x , event.y , outline = cor_principal)

    elif formato_principal == "oval" :
        fig = canvas.create_oval(ini_x , ini_y , event.x , event.y , outline = cor_principal)

    elif formato_principal == "circulo" :
        raio = min(abs(event.x - ini_x), abs(event.y - ini_y))
        x_final = ini_x + raio if event.x >= ini_x else ini_x - raio
        y_final = ini_y + raio if event.y >= ini_y else ini_y - raio # iguala a altura com a largura ao buscar a menor distância

        fig = canvas.create_oval(ini_x, ini_y, x_final, y_final, outline = cor_principal )

    elif formato_principal == "linha" :
        fig = canvas.create_line(ini_x , ini_y , event.x, event.y, fill = cor_principal, width = 3)
    
    elif formato_principal == "rabisco" :
        canvas.create_line(atualizar.x_antigo, atualizar.y_antigo, event.x, event.y, fill= cor_principal , width = 3)
        # união dos pontos
        atualizar.x_antigo = event.x
        atualizar.y_antigo = event.y

# soltar o mouse 

def soltar_mouse(event) :
    global fig 
    fig = None

    # termina o desenho da figura

#---------MAIN-----------#

janela = Tk()
janela.title("Paint da Mi e do Gui")
titulo = Label(janela, text = ".✦ ݁˖Paint da Mi e do Gui.✦ ݁˖" , font = ("Times New Roman", 20))
titulo.pack()
canvas = Canvas(janela, bg = "white" , width = 800, height = 800)
canvas.pack()

# menu
fig_var = StringVar() # guarda a str pra executar a função
fig_var.set("retangulo")

def mudar_fig(*args):
    global formato_principal
    formato_principal = fig_var.get() # executa os diferentes tipos de variáveis que o usuário escolher


fig_var.trace_add("write", mudar_fig) # executa a função quando a variável mudar

menu = Menu(janela)
janela.config(menu= menu)
# CRIA UMA BARRA DE MENU NA PARTE SUPERIOR

menudasfigs = Menu(menu , tearoff = 0) # menu interno | tearoff = retira a linha pontilhada que poderia aparecer no menu

menu.add_cascade(label = "Selecionar figura" , menu = menudasfigs) # permite que o usuário clique em "Selecionar figura" e o menu interno apareça
menudasfigs.add_radiobutton(label="Retângulo" , variable = fig_var , value = "retangulo")
menudasfigs.add_radiobutton(label="Círculo" , variable = fig_var , value = "circulo")
menudasfigs.add_radiobutton(label = "Oval" , variable = fig_var , value = "oval")
menudasfigs.add_radiobutton(label = "Rabisco" , variable = fig_var , value = "rabisco")
menudasfigs.add_radiobutton(label = "Linha" , variable = fig_var , value = "linha" )
# permite que o usuário clique em UMA das opções e as funções responsáveis por cada figura sejam chamadas e executadas

canvas.bind("<Button-1>", iniciar_mouse)
canvas.bind("<B1-Motion>", atualizar)
canvas.bind("<ButtonRelease-1>", soltar_mouse)

janela.mainloop()