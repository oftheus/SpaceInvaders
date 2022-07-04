from PPlay.gameimage import *
from PPlay.window import *

janela = Window(800, 600)
janela.set_title('Space Invaders')
fundo = GameImage("fundo.jpg")
galaxia = GameImage("galaxia.jpg")

cdTempo = 0
GAME_STATE = 0
dif = 1
FASE = 1
pontos_da_nave = 0