from model.desenho import PaintModel
from view.janelaPaint import PaintView
from controller.controlador import PaintController


def main():

    model = PaintModel()

    view = PaintView()

    controller = PaintController(model, view)

    view.mainloop()


main()