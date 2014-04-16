from turtle import Screen, Turtle, Pen
import os, time
from glob import glob

LARG_BALAO=24


def carregaimagens(caminho = str, janela = Screen):
    dir_atual = os.getcwd()
    os.chdir(caminho)
    for img in glob('*.gif'):
        janela.addshape(img)
    os.chdir(dir_atual)


def formata(texto = str):
    if len(texto) > LARG_BALAO:
        trechos = []
        resto = ''
        for i in range(len(texto)//LARG_BALAO):
            trecho = resto + texto[LARG_BALAO*i:LARG_BALAO*(i+1)]
            pos_ult_espaco = trecho.rfind(' ')
            pedaco = trecho[:pos_ult_espaco]
            resto = trecho[pos_ult_espaco:]
            pedaco = pedaco.strip()
            trechos.append(pedaco)
        texto = '\n'.join(trechos)
    return texto


class Digimon:
    def __init__(self, nome = str, exibir=True):
        self._img = Pen()
        self._img.up()        
        self._img.shape(nome+'.gif')
        print(nome+'.gif')
        self._img.speed('fastest')
        self._caneta = Pen()
        self._caneta.hideturtle()
        self._caneta.pensize(2)
        self._caneta.color('white')
        if not exibir:
            self._img.hideturtle()
        



                
    def falar(self, mensagem = str):
        #mensagem = formata(mensagem)
        x,y = self._img.position()
        self._caneta.up()
        self._caneta.goto(x,y)
        self._caneta.down()
        self._caneta.goto(x+100,y+100)
        self._caneta.write(mensagem)
        time.sleep(3)
        self._caneta.clear()


    def esconder(self):
        self._img.hideturtle()

    def exibir(self):
        self._img.showturtle()

    def andar_direita(self, distancia = int):
        self._img.forward(distancia)

    def andar_esquerda(self, distancia = int):
        self._img.left(180)
        self._img.forward(distancia)
        
    def vapara (self, x = int, y =int):
        self._img.goto(x, y)


    def pular_cima (self):
        x,y = self._img.position()
        self._img.goto(x, y+100)
        time.sleep(0.5)
        self._img.goto(x+50, y-100)


    def pular_tras (self):
        x,y = self._img.position()
        self._img.goto(x-100, y+100)
        time.sleep(0.5)
        self._img.goto(x-100, y-100)


    def pular_frente (self):
        x,y = self._img.position()
        self._img.goto(x+100, y+100)
        time.sleep(0.5)
        self._img.goto(x+100, y-100)

    def posicao(self):
        return self._img.position()
            
        
    def lancar(self, vx = int, vy = int):
        x,y = self.posicao()
        for i in range(20):          
            self.vapara(x+i*vx, y+i*vy)
            vy -= 1
        

