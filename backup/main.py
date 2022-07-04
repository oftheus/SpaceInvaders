import dados
from menu import Menu
from tela_dificuldades import TelaDificuldades
from jogo import Jogar

def main():
    def setup():
        menu = Menu(dados.janela, dados.fundo)
        jogo = Jogar(dados.janela, dados.galaxia)
        telaDificuldades = TelaDificuldades(dados.janela, dados.fundo)
        return menu,jogo,telaDificuldades

    while True:
        if dados.GAME_STATE == 0:
            dados.dif = 1
            dados.FASE = 1
            menu,jogo,telaDificuldades = setup()
            dados.GAME_STATE = 1

        elif dados.GAME_STATE == 1:
            menu.run()
        elif dados.GAME_STATE == 2:
            jogo.run()
        elif dados.GAME_STATE == 3:
            telaDificuldades.run()

        elif dados.GAME_STATE == 4:
            menu, jogo, telaDificuldades = setup()
            dados.GAME_STATE = 2

        elif dados.GAME_STATE == 5:
            dados.janela.close()

        dados.cdTempo += dados.janela.delta_time()
        dados.janela.update()

main()