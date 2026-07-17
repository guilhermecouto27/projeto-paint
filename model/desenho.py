import pickle
import copy

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

        # Indice da figura selecionada
        self.__selecionada = -1   

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
        for i in range(len(self.__formas)):
            if i == self.__selecionada :
                self.__formas[i].desenha(canvas, dash=(10, 1), width=4)
            else :
                self.__formas[i].desenha(canvas)


    def limpa_selecao(self) :
        self.__selecionada = -1

    def seleciona(self, px, py) :
        i = len(self.__formas)-1
        while i >= 0 and not self.__formas[i].contem(px, py) :
            i -= 1
        self.__selecionada = i

    def selecionada(self) :
        if self.__selecionada >= 0 :
            return self.__formas[self.__selecionada]
        else :
            return None
        
        # Copiar/Colar
    def copiar_selecionada(self) :
        self.buffer = copy.deepcopy(self.selecionada())

    def colar(self) :
        if self.buffer != None :
            f = self.buffer
            f.mover(5, 5)
            self.__formas.append(f)
            self.buffer = copy.deepcopy(f)

        #**** Operações sobre a figura selecionada

    def selecionada_para_topo(self) :
        s = self.__selecionada 
        if s != -1 :
            f = self.__formas.pop(s)
            self.__formas.append(f)
            self.__selecionada = len(self.__formas)-1
        
    def selecionada_para_fundo(self) :
        s = self.__selecionada 
        if s != -1 :
            f = self.__formas.pop(s)
            self.__formas.insert(0, f)
            self.__selecionada = 0

    def selecionada_para_tras(self) :
        s = self.__selecionada 
        if s > 0 :
            self.__formas[s], self.__formas[s-1] = self.__formas[s-1], self.__formas[s]
            self.__selecionada -= 1

    def selecionada_para_frente(self) :
        s = self.__selecionada 
        if 0 <= s < len(self.__formas) - 1 :
            self.__formas[s], self.__formas[s+1] = self.__formas[s+1], self.__formas[s]
            self.__selecionada += 1

    def apaga_selecionada(self) :
        s = self.__selecionada 
        if s != -1 :
            self.__formas.pop(s)
            self.__selecionada = -1

    # Persistência com pickle

    def salvar(self, caminho):
        with open(caminho, "wb") as arquivo:
            pickle.dump(self.__formas, arquivo)

    def abrir(self, caminho):
        with open(caminho, "rb") as arquivo:
            self.__formas = pickle.load(arquivo)