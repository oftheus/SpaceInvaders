import configs
from player import Nave
from inimigos import Inimigos

class Jogar:
    def __init__(self, janela, galaxia):
        self.janela = janela
        self.galaxia = galaxia
        self.teclado = janela.get_keyboard()
        self.nave = Nave(self.janela)
        self.monstros = Inimigos(self.janela, self.nave)
        self.tempo = 0
        self.fps = 0
        self.frameRate = 0

    def adicionaPontuacaoRanking(self, usuario, pontos):
        from os import remove, rename
        configs_do_ranking = open("rankingPontos", "r", encoding="utf-8")
        configs_do_rankingTemp = open("rankingPontos"+"$$$", "w", encoding="utf-8")
        escreveu = False

        for linha in configs_do_ranking:
            nome, pts = linha.strip("\n").split("#")
            pts = int(pts)
            if pts<pontos and not escreveu:
                configs_do_rankingTemp.write(usuario + "#" + str(pontos) + "\n")
                escreveu = True
            configs_do_rankingTemp.write(nome + "#" + str(pts) + "\n")

        if not escreveu:
            configs_do_rankingTemp.write(usuario + "#" + str(pontos) + "\n")

        configs_do_ranking.close()
        configs_do_rankingTemp.close()
        remove("rankingPontos")
        rename("rankingPontos" + "$$$", "rankingPontos")
        return None

    def run(self):
        self.galaxia.draw()
        self.janela.draw_text(str(configs.pontos_da_nave), self.janela.width / 2 - 25, 5, size=30, color=(205, 205, 205), font_name="arial", bold=True,italic=False)
        self.janela.draw_text("fps: "+str(self.frameRate), 10, 5, size=20, color=(205, 205, 205), font_name="arial",bold=False, italic=True)
        self.janela.draw_text("FASE " + str(configs.fases), self.janela.width - 80, 45, size=15, color=(205, 205, 205),font_name="arial", bold=True, italic=False)
        self.nave.run()
        self.monstros.run()
        self.tempo += self.janela.delta_time()
        self.fps += 1
        if self.tempo >= 1:
            self.frameRate = self.fps
            self.tempo = 0
            self.fps = 1

        if not self.monstros.inimigos:
            configs.estado = 4
            configs.fases += 1

        if not self.nave.vidasNave or self.monstros.check_colidiuNave:
            usuario = input("Digite seu nome: ")
            self.adicionaPontuacaoRanking(usuario, configs.pontos_da_nave)
            configs.pontos_da_nave = 0
            configs.estado = 0

        if self.teclado.key_pressed('ESC'):
            configs.estado = 0