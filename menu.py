import configs
from PPlay.gameimage import *

class Menu:
    def __init__(self, janela, fundo):
        self.janela = janela
        self.fundo = fundo
        self.mouse = janela.get_mouse()
        janela.set_title("Space Invaders")
        icone = pygame.image.load('./imagens/nave.png')
        pygame.display.set_icon(icone)

        self.botao_jogar = GameImage("./imagens/jogar.png")
        self.botao_dificuldade = GameImage("./imagens/dificuldade.png")
        self.botao_ranking = GameImage("./imagens/ranking.png")
        self.botao_sair = GameImage("./imagens/sair.png")

        self.titulo = GameImage("./imagens/titulo.png")
        self.titulo.set_position(self.janela.width/2 - self.titulo.width/2,30)
        self.botao_jogar.set_position(self.janela.width/2 - self.botao_jogar.width/2,230)
        self.botao_dificuldade.set_position(self.janela.width/2 - self.botao_dificuldade.width/2,300)
        self.botao_ranking.set_position(self.janela.width/2 - self.botao_ranking.width/2,370)
        self.botao_sair.set_position(self.janela.width/2 - self.botao_sair.width/2, 440)

    def run(self):

        self.fundo.draw()
        self.botao_jogar.draw()
        self.botao_dificuldade.draw()
        self.botao_ranking.draw()
        self.botao_sair.draw()
        self.titulo.draw()

        if configs.tempo >= 0.5:
            if self.mouse.is_over_object(self.botao_jogar):
                if self.mouse.is_button_pressed(1):
                    configs.tempo = 0
                    configs.estado = 2

            if self.mouse.is_over_object(self.botao_dificuldade):
                if self.mouse.is_button_pressed(1):
                    configs.tempo = 0
                    configs.estado = 3

            if self.mouse.is_over_object(self.botao_ranking):
                if self.mouse.is_button_pressed(1):
                    configs.tempo = 0
                    configs.estado = 6

            if self.mouse.is_over_object(self.botao_sair):
                if self.mouse.is_button_pressed(1):
                    configs.tempo = 0
                    configs.estado = 5