from abc import ABC, abstractmethod

from dataclasses import dataclass, field
#criando a classe principal FIGURA para que os mesmos métodos dela sejam utilizados nas outras classes(que também são figuras)
class Figura(ABC):
    @abstractmethod
    def desenha(self, canvas, preview=False):
        pass

    @abstractmethod
    def vazia(self):
        return False # as figuras precisam desenhar e identificar quando estão vazias
