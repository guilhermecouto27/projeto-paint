import pickle

class PaintModel:

    def __init__(self):

        # posição inicial do mouse
        self.x = None
        self.y = None

        # figura temporária
        self.fig = None

        # figura selecionada
        self.formato_principal = "retangulo"

        # cor da borda
        self.cor_principal = "black"

        # cor do preenchimento
        self.cor_preenchimento = ""

        # figuras desenhadas
        self.__formas = []

        # pontos do rabisco
        self.pontos_rabisco = []

    # métodos para manipular as figuras desenhadas
    def mudar_cor(self, cor):
        self.cor_principal = cor

    # métodos para manipular as figuras desenhadas
    def mudar_preenchimento(self, cor):
        self.cor_preenchimento = cor

    # métodos para manipular as figuras desenhadas
    def mudar_forma(self, forma):
        self.formato_principal = forma
    
    # métodos para manipular as figuras desenhadas
    def adiciona_figura(self, figura):
        self.__formas.append(figura)

    # métodos para manipular as figuras desenhadas
    def desenha_figuras(self, canvas, dash=()):
        canvas.delete("all")
        for figura in self.__formas:
            figura.desenha(canvas, dash=dash)

    # Persistência com pickle

    def salvar(self, caminho):
        with open(caminho, "wb") as arquivo:
            pickle.dump(self.__formas, arquivo)

    def abrir(self, caminho):
        with open(caminho, "rb") as arquivo:
            self.__formas = pickle.load(arquivo)