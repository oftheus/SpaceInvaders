from PPlay.gameimage import *
from PPlay.window import *

janela = Window(800, 600)
janela.set_title('Space Invaders')
fundo = GameImage("./imagens/fundo.jpg")
galaxia = GameImage("./imagens/galaxia.jpg")

tempo = 0
estado = 0
dif = 1
fases = 1
pontos_da_nave = 0