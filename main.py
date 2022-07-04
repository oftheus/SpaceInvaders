import configs
from menu import Menu
from tela_dificuldades import Dificuldades
from jogo import Jogar
from ranking import Ranking

def main():
    def setup():
        menu = Menu(configs.janela, configs.fundo)
        jogo = Jogar(configs.janela, configs.galaxia)
        dif = Dificuldades(configs.janela, configs.fundo)
        ranking = Ranking(configs.janela, configs.fundo)
        return menu,jogo,dif,ranking

    while True:
        if configs.estado == 0:
            configs.dif = 1
            configs.fases = 1
            menu,jogo,dif,ranking = setup()
            configs.estado = 1

        elif configs.estado == 1:
            menu.run()
        elif configs.estado == 2:
            jogo.run()
        elif configs.estado == 3:
            dif.run()
        elif configs.estado == 6:
            ranking.run()

        elif configs.estado == 4:
            menu, jogo, dif, ranking = setup()
            configs.estado = 2

        elif configs.estado == 5:
            configs.janela.close()

        configs.tempo += configs.janela.delta_time()
        configs.janela.update()

main()