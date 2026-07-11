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
        self.formas = []

        # pontos do rabisco
        self.pontos_rabisco = []

    def mudar_cor(self, cor):
        self.cor_principal = cor

    def mudar_preenchimento(self, cor):
        self.cor_preenchimento = cor

    def mudar_forma(self, forma):
        self.formato_principal = forma
