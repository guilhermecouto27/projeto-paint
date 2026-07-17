from dataclasses import dataclass
from view.janelaPaint import PaintView
from model.desenho import PaintModel

@dataclass
class ControladorSelecao : 
    visao : PaintView
    desenho : PaintModel

    def __post_init__(self) :
       # self.visao.widget_cor_linha.bind(self.atualiza_cor_linha)
       # self.visao.widget_cor_pree.bind(self.atualiza_cor_preenchimento)
        
        root = self.visao

        atua_com = self.atua_com
        root.bind("<Up>", self.atua_com(self.desenho.selecionada_para_topo))
        root.bind("<Down>", self.atua_com(self.desenho.selecionada_para_fundo))
        root.bind("<Left>", self.atua_com(self.desenho.selecionada_para_tras))
        root.bind("<Right>", self.atua_com(self.desenho.selecionada_para_frente))
        root.bind("<Control-c>", self.atua_com(self.desenho.copiar_selecionada))
        root.bind("<Control-v>", self.atua_com(self.desenho.colar))
        root.bind("<Delete>", self.atua_com(self.desenho.apaga_selecionada))

   # def atualiza_cor_linha(self) :
       # f = self.desenho.selecionada() 
       # if f != None :
          #  f.cor_borda = self.visao.cor_linha()
           # self.desenho.desenha_figuras(self.visao.canvas)
        
    #def atualiza_cor_preenchimento(self) :
      #  f = self.desenho.selecionada() 
      #  if f != None :
           # f.cor_preenchimento = self.visao.cor_preenchimento()
          #  self.desenho.desenha_figuras(self.visao.canvas)

    def atua_com(self, atua) :
        def ignoraEvent(event) :
            atua()
            self.desenho.desenha_figuras(self.visao.canvas)
        return ignoraEvent