import configs
from PPlay.sprite import *
from random import randint

class Inimigos:
    def __init__(self, janela, nave):
        self.janela = janela
        self.linhas_invaders = min(2 + (1*configs.fases), 4)
        self.colunas_invaders = min(3 + (2*configs.fases), 6)
        self.inimigos = []
        self.velocidade_monstro_X = 30 + 30*configs.dif + 20*configs.fases
        self.velocidade_monstro_Y = 25
        self.tempo_para_descer = 0
        self.nave = nave
        self.tempo_invencivel = 0
        self.check_danoNave = False
        self.check_colidiuNave = False
        self.velocidade_tiro_nave = 200 + (10 * configs.dif)
        self.tempo_de_recarga_tiro = 0
        self.diminuitempo_de_recarga_tiro = 0
        self.tempo_do_tiro = randint(30-10*configs.fases, 200-20*configs.fases)/100
        self.tiro_dos_monstros = []
        self.criar_inimigos()

    def criar_inimigos(self):
        for l in range(self.linhas_invaders):
            for c in range(self.colunas_invaders):
                monstro = Sprite("./imagens/inimigo.png", 1)
                if c == 0:
                    monstro.x = self.janela.width / 2 - (self.colunas_invaders / 2 * monstro.width)
                    monstro.y = (l + 1.8) * monstro.height
                else:
                    monstro.x = self.inimigos[c - 1].x + monstro.width * 3 / 2
                    monstro.y = (l + 1.8) * monstro.height
                self.inimigos.append(monstro)

    def colidiu(self):
        for m in self.inimigos:
            if m.x >= self.janela.width - m.width or m.x<=0:
                return 1
        return 0

    def movimentaInimigos(self):
        self.tempo_para_descer += self.janela.delta_time()

        for m in self.inimigos:
            m.x += self.velocidade_monstro_X * self.janela.delta_time()

        if self.tempo_para_descer > 0.15:
            if self.colidiu():
                for monstro in self.inimigos:
                    monstro.y += self.velocidade_monstro_Y
                self.velocidade_monstro_X *= (-1)
                self.tempo_para_descer = 0

    def detectaMorteMonstro(self):
        colidiu = False
        for tiro in self.nave.tiros:
            if self.inimigos[0].y <= tiro.y <= self.inimigos[-1].y+self.inimigos[-1].height:
                for mon in self.inimigos:
                    if tiro.collided(mon):
                        if self.velocidade_monstro_X > 0:
                            self.velocidade_monstro_X += 8 + 2*configs.fases
                        if self.velocidade_monstro_X < 0:
                            self.velocidade_monstro_X -= 8 + 2*configs.fases
                        self.diminuitempo_de_recarga_tiro += 5
                        self.nave.tiros.remove(tiro)
                        self.inimigos.remove(mon)
                        configs.pontos_da_nave += 1
                        colidiu = True
                        break
                if colidiu:
                    break

    def detectaDanoNave(self):
        for tiro in self.tiro_dos_monstros:
            if (self.nave.nave.y <= tiro.y <= self.nave.nave.y + self.nave.nave.height) and not self.check_danoNave:
                if tiro.collided(self.nave.nave):
                    self.tiro_dos_monstros.remove(tiro)
                    self.nave.vidasNave.pop(-1)
                    self.check_danoNave = True
                    self.tempo_invencivel = 0
                    self.nave.nave.set_position(self.janela.width / 2 - self.nave.nave.width / 2,self.janela.height - self.nave.nave.height * 1.25)
                    break

    def piscaNave(self):
        if self.tempo_invencivel <= 2:
            self.tempo_invencivel += self.janela.delta_time()
            if 0 <= self.tempo_invencivel <= 0.4 or 0.7 <= self.tempo_invencivel <= 1.1 or \
                    1.4 <= self.tempo_invencivel <= 1.7:
                coordenadas_anteriores = (self.nave.nave.x, self.nave.nave.y)
                self.nave.nave = Sprite("./imagens/piscando.png")
                self.nave.nave.set_position(coordenadas_anteriores[0], coordenadas_anteriores[1])
            else:
                coordenadas_anteriores = (self.nave.nave.x, self.nave.nave.y)
                self.nave.nave = Sprite("./imagens/nave.png")
                self.nave.nave.set_position(coordenadas_anteriores[0], coordenadas_anteriores[1])
        else:
            self.check_danoNave = False

    def atiraMonstro(self):
        atira_monstros = randint(0, len(self.inimigos)-1)
        tiros_dado = Sprite("./imagens/bala2.png", 1)
        tiros_dado.x = self.inimigos[atira_monstros].x + self.inimigos[atira_monstros].width / 2 - tiros_dado.width / 2
        tiros_dado.y = self.inimigos[atira_monstros].y + self.inimigos[atira_monstros].height
        self.tiro_dos_monstros.append(tiros_dado)
        self.tempo_de_recarga_tiro = 0
        self.tempo_do_tiro = randint(max(20,(80-10*configs.fases-self.diminuitempo_de_recarga_tiro)),max(100,(230-30*configs.fases-self.diminuitempo_de_recarga_tiro)))/100

    def movimentaTiros(self):
        for tiro in self.tiro_dos_monstros:
            if tiro.y + tiro.height >= self.janela.height:
                self.tiro_dos_monstros.remove(tiro)
            tiro.y += self.velocidade_tiro_nave*self.janela.delta_time()

    def run(self):
        for i in self.inimigos:
            i.draw()
        for t in self.tiro_dos_monstros:
            t.draw()

        self.tempo_de_recarga_tiro += self.janela.delta_time()

        if self.inimigos[-1].y + self.inimigos[-1].height >= self.nave.nave.y:
            self.check_colidiuNave = True

        if self.tempo_de_recarga_tiro >= self.tempo_do_tiro:
            self.atiraMonstro()

        self.detectaMorteMonstro()
        self.detectaDanoNave()

        if self.check_danoNave:
            self.piscaNave()

        self.movimentaTiros()
        self.movimentaInimigos()