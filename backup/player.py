import dados
from PPlay.gameimage import *
from PPlay.sprite import *

class Nave:
    def __init__(self, janela):
        self.janela = janela
        self.nave = Sprite("nave.png")

        self.nave.set_position(janela.width/2 - self.nave.width/2, janela.height - self.nave.height*1.25)
        self.tiros = []
        self.teclado = janela.get_keyboard()
        self.velNave = 250 - (30*dados.dif) + (30*dados.FASE)
        self.velTiro = 350 - (20*dados.dif) + (50*dados.FASE)
        self.countTempo = 0

    def controlaNave(self):
        if self.teclado.key_pressed("A") and self.nave.x >= 0:
            self.nave.x -= self.velNave * self.janela.delta_time()
        if self.teclado.key_pressed("D") and self.nave.x <= self.janela.width - self.nave.width:
            self.nave.x += self.velNave * self.janela.delta_time()

        if self.teclado.key_pressed("SPACE") and self.countTempo > (0.5 + 0.1 * dados.dif - (min(0.07 * dados.FASE, 0.3))):
            tiroCriado = Sprite("bala.png", 1)
            tiroCriado.x = self.nave.x + self.nave.width / 2 - tiroCriado.width / 2
            tiroCriado.y = self.nave.y - tiroCriado.height
            self.tiros.append(tiroCriado)
            self.countTempo = 0

    def run(self):
        self.nave.draw()
        for t in self.tiros:
            t.draw()
        self.countTempo += self.janela.delta_time()
        self.controlaNave()

        for tiro in self.tiros:
            if tiro.y <= 0:
                self.tiros.remove(tiro)
            tiro.y -= self.velTiro * self.janela.delta_time()