import configs
from PPlay.gameimage import *
from PPlay.sprite import *

class Nave:
    def __init__(self, janela):
        self.janela = janela
        self.nave = Sprite("./imagens/nave.png")

        self.nave.set_position(janela.width/2 - self.nave.width/2, janela.height - self.nave.height*1.25)
        self.tiros = []
        self.teclado = janela.get_keyboard()
        self.velocidade_nave = 250 - (30*configs.dif) + (30*configs.fases)
        self.velocidade_tiro = 350 - (20*configs.dif) + (50*configs.fases)
        self.vidasNave=[]
        self.quantidade_de_vidas=5
        self.tempo = 0
        self.iniciaVidas()

    def iniciaVidas(self):
        for v in range(self.quantidade_de_vidas):
            vida = GameImage("./imagens/heart.png")
            vida.x = (v + 26) * vida.width + v * 5
            vida.y = 10
            self.vidasNave.append(vida)

    def controlaNave(self):
        if self.teclado.key_pressed("A") and self.nave.x >= 0:
            self.nave.x -= self.velocidade_nave * self.janela.delta_time()
        if self.teclado.key_pressed("D") and self.nave.x <= self.janela.width - self.nave.width:
            self.nave.x += self.velocidade_nave * self.janela.delta_time()

        if self.teclado.key_pressed("SPACE") and self.tempo > (0.5 + 0.1 * configs.dif - (min(0.07 * configs.fases, 0.3))):
            tiros_dado = Sprite("./imagens/bala.png", 1)
            tiros_dado.x = self.nave.x + self.nave.width / 2 - tiros_dado.width / 2
            tiros_dado.y = self.nave.y - tiros_dado.height
            self.tiros.append(tiros_dado)
            self.tempo = 0

    def run(self):
        self.nave.draw()
        for t in self.tiros:
            t.draw()
        for v in self.vidasNave:
            v.draw()

        self.tempo += self.janela.delta_time()
        self.controlaNave()

        for tiro in self.tiros:
            if tiro.y <= 0:
                self.tiros.remove(tiro)
            tiro.y -= self.velocidade_tiro * self.janela.delta_time()