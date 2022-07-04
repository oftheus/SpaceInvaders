from PPlay.gameimage import *
import configs


class Ranking:
    def __init__(self, janela, fundo):
        self.janela = janela
        self.fundo = fundo
        self.teclado = janela.get_keyboard()

        self.rankingTitulo = GameImage("./imagens/ranking.png")
        self.rankingTitulo.set_position(self.janela.width / 2 - self.rankingTitulo.width / 2, self.rankingTitulo.height)
        self.ranking = []
        self.pegaRanking()

    def pegaRanking(self):
        configs = open("rankingPontos", "r", encoding="utf-8")
        linha = configs.readline()
        if linha != "":
            while len(self.ranking) < 5 and linha != "":
                nome, pts = linha.strip("\n").split("#")
                self.ranking.append((nome, pts))
                linha = configs.readline()

        configs.close()

    def run(self):
        self.fundo.draw()
        self.rankingTitulo.draw()
        for i in range(len(self.ranking)):
            self.janela.draw_text(str(i+1) + " - " + self.ranking[i][0] + ", " + self.ranking[i][1] + " pontos",
                                  self.janela.width / 2 - 120, 200 + 50*(i+1), size=30, color=(205, 205, 205),
                                  font_name="arial", bold=True, italic=True)

        if self.teclado.key_pressed('ESC'):
            configs.estado = 0