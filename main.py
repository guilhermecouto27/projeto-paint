from model.desenho import PaintModel
from view.janelaPaint import PaintView
from controller.controller import ControladorPaint

# Função principal que inicializa o modelo, a visão e o controlador do aplicativo de desenho
def main():

    desenho = PaintModel()

    visao = PaintView()

    controller = ControladorPaint(visao, desenho)

    visao.mainloop()


main()