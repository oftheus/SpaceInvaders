import dados
from player import Nave
from PPlay.gameimage import *
from PPlay.mouse import *

class Jogar:
    def __init__(self, janela, galaxia):
        self.janela = janela
        self.galaxia = galaxia
        self.teclado = janela.get_keyboard()
        self.nave = Nave(self.janela)

        self.countTempo = 0
        self.countFrame = 0
        self.frameRate = 0

    def run(self):
        self.galaxia.draw()
        if self.teclado.key_pressed('ESC'):
            dados.GAME_STATE = 0

        self.janela.draw_text("fps: "+str(self.frameRate), 10, 5, size=20, color=(205, 205, 205), font_name="arial",bold=False, italic=True)

        self.nave.run()

        self.countTempo += self.janela.delta_time()
        self.countFrame += 1
        if self.countTempo >= 1:
            self.frameRate = self.countFrame
            self.countTempo = 0
            self.countFrame = 1

        if self.teclado.key_pressed('ESC'):
            dados.GAME_STATE = 0