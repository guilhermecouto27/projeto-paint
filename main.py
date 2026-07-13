from model.desenho import PaintModel
from view.janelaPaint import PaintView
from controller.controller import ControladorPaint


def main():

    desenho = PaintModel()

    visao = PaintView()

    controller = ControladorPaint(visao, desenho)

    visao.mainloop()


main()