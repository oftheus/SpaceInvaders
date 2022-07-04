import configs
from PPlay.gameimage import *

class Dificuldades:
    def __init__(self, janela, fundo):
        self.janela = janela
        self.fundo = fundo
        self.mouse = janela.get_mouse()

        self.botao_facil = GameImage("./imagens/facil.png")
        self.botao_medio = GameImage("./imagens/medio.png")
        self.botao_dificil = GameImage("./imagens/dificil.png")

        self.botao_facil.set_position(self.janela.width/2 - self.botao_facil.width/2, 230)
        self.botao_medio.set_position(self.janela.width/2 - self.botao_medio.width/2, 300)
        self.botao_dificil.set_position(self.janela.width/2 - self.botao_dificil.width/2, 370)

    def run(self):

        self.fundo.draw()
        self.botao_facil.draw()
        self.botao_medio.draw()
        self.botao_dificil.draw()

        if configs.tempo >= 0.5:
            if self.mouse.is_over_object(self.botao_facil):
                if self.mouse.is_button_pressed(1):
                    configs.tempo = 0
                    configs.dif = 1
                    configs.estado = 1

            if self.mouse.is_over_object(self.botao_medio):
                if self.mouse.is_button_pressed(1):
                    configs.tempo = 0
                    configs.dif = 1.5
                    configs.estado = 1

            if self.mouse.is_over_object(self.botao_dificil):
                if self.mouse.is_button_pressed(1):
                    configs.tempo = 0
                    configs.dif = 2
                    configs.estado = 1
