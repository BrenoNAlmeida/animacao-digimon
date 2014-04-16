#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import Screen
from digimon import Digimon, carregaimagens
from personagem import Personagem, carregaimagens
import time

#Método para criar todos os personagens como variáveis globais.
#Todas as imagens serão carregadas de uma vez.
def cria_personagens():

    global koromon
    koromon = Digimon('koromon', exibir=False)
    global tai
    tai = Personagem('tai', exibir=False)
    
    global tsunomon
    tsunomon = Digimon('tsunomon', exibir=False)
    global matt
    matt = Personagem('matt', exibir=False)
    
    global motimon
    motimon = Digimon('motimon', exibir=False)
    global izzy
    izzy = Personagem('izzy', exibir=False)

    global yokomon
    yokomon = Digimon('yokomon', exibir=False)
    global sora
    sora = Personagem('sora', exibir=False)

    global bukamon
    bukamon = Digimon('bukamon', exibir=False)
    global joe
    joe = Personagem('joe', exibir=False)

    global tanemon
    tanemon = Digimon('tanemon', exibir=False)
    global mimi
    mimi = Personagem('mimi', exibir=False)

    global tokomon
    tokomon = Digimon('tokomon', exibir=False)
    global tk
    tk = Personagem('tk', exibir=False)


    
#Início dos atos: a partir daqui, o programa em si vai começar a ser
#estruturado. Aqui, será criado um ato para apresentação do digimon
#com seu respectivo owner.

    
def abertura(janela = Screen):
    janela.title('Abertura')
    janela.bgpic('fundos/inicio.gif')
    janela.bgcolor('white')
    time.sleep(1.5)

def ato2(janela = Screen):
    janela.title("Tai e Koromon")
    janela.bgpic('fundos/floresta.gif')
    tai.exibir()
    tai.vapara(-200, 0)
    tai.falar('Olá, meu nome é Tai!')
    koromon.exibir()
    koromon.andar_direita(50)
    koromon.falar('Olá, meu nome é Koromon!')
    koromon.pular_cima()
    koromon.falar('Esperei muito tempo por você, Tai!')
    time.sleep(1.5)
    tai.esconder()
    koromon.esconder()

def ato3(janela = Screen):
    janela.title("Matt e Tsunomon")
    janela.bgpic('fundos/floresta.gif')
    matt.exibir()
    matt.vapara(150, 0)
    matt.falar('E aí, meu nome é Matt!')
    tsunomon.exibir()
    tsunomon.andar_esquerda(200)
    tsunomon.falar('Olá, Matt, meu nome é Tsunomon!')
    tsunomon.pular_cima()
    tsunomon.andar_esquerda(250)
    tsunomon.falar('Agora, serei seu mais novo amigo!')
    matt.falar('rsrs')
    time.sleep(1.5)
    matt.esconder()
    tsunomon.esconder()


def ato4(janela = Screen):
    janela.title("Izzy e Motimon")
    janela.bgpic('fundos/floresta.gif')
    izzy.exibir()
    izzy.vapara(150,0)
    izzy.falar('Oi! Meu nome é Izzy')
    motimon.exibir()
    motimon.vapara(-150, 0)
    motimon.falar('Oi, Izzy! Meu nome é Motimon!')
    motimon.andar_direita(50)
    motimon.falar('Sou seu digiamigo :D !')
    time.sleep(1.5)
    izzy.esconder()
    motimon.esconder()

def ato5(janela = Screen):
    janela.title("Sora e Yokomon")
    janela.bgpic('fundos/floresta.gif')
    sora.exibir()
    sora.vapara(-200,0)
    sora.falar('Olá, pessoal. Meu nome é Sora.')
    yokomon.exibir()
    yokomon.pular_cima()
    yokomon.andar_esquerda(50)
    yokomon.falar('Sora, esperei tanto por você!!')
    time.sleep(1.5)
    sora.esconder()
    yokomon.esconder()


def ato6(janela = Screen):
    janela.title("Joe e Bukamon")
    janela.bgpic('fundos/floresta.gif')
    joe.exibir()
    joe.falar('Olá, eu sou o Joe.')
    joe.andar_direita(150)
    bukamon.exibir()
    bukamon.pular_cima()
    bukamon.andar_esquerda(150)
    bukamon.falar('Eu já amo você, Joe!!')
    joe.falar('Eca, sai pra lá!')
    time.sleep(1.5)
    joe.esconder()
    bukamon.esconder()

def ato7(janela = Screen):
    janela.title("Mimi e Tanemon")
    janela.bgpic('fundos/floresta.gif')
    mimi.exibir()
    mimi.vapara(100,0)
    mimi.falar('Oi gente *-* Meu nome é Mimi.')
    tanemon.exibir()
    tanemon.andar_esquerda(300)
    tanemon.falar('Mimi, sou Tanemom Somos lindas né *-*!')
    tanemon.pular_cima()
    tanemon.andar_direita(50)
    tanemon.falar('Vamos nos dar muito bem :D !')
    time.sleep(1.5)
    mimi.esconder()
    tanemon.esconder()

def ato8(janela = Screen):
    janela.title("T.K. e Tokomon")
    janela.bgpic('fundos/floresta.gif')
    tk.exibir()
    tk.vapara(-250,0)
    tk.falar('Oi, todo mundo! Aqui é o T.K.')
    tokomon.exibir()
    tokomon.pular_cima()
    tokomon.falar('Olá, T.K. Eu sou Tokomon!!')
    tokomon.pular_frente()
    tokomon.falar('Sou seu digiamigo :D !')
    time.sleep(1.5)
    tk.esconder()
    tokomon.esconder()
    

#Nessa 'finale', temos um 'album de fotos dos digimons com seus donos.
    
def finale(janela = Screen):
    janela.title('Tai e Koromon!')
    janela.bgpic('digimonftowners/taiftkoromon.gif')
    time.sleep(2)
    janela.title('Matt e Tsunomon!')
    janela.bgpic('digimonftowners/mattfttsunomon.gif')
    time.sleep(2)
    janela.title('Izzy e Motimon!')
    janela.bgpic('digimonftowners/izzyftmotimon.gif')
    time.sleep(2)
    janela.title('Sora e Yokomon!')
    janela.bgpic('digimonftowners/soraftyokomon.gif')
    time.sleep(2)
    janela.title('Joe e Bukamon!')
    janela.bgpic('digimonftowners/joeftbukamon.gif')
    time.sleep(2)
    janela.title('Mimi e Tanemon!')
    janela.bgpic('digimonftowners/mimifttanemon.gif')
    time.sleep(2)
    janela.title('T.K. e Tokomon!')
    janela.bgpic('digimonftowners/tkfttokomon.gif')
    time.sleep(2)

#Encerramento da animação
    
def fechamento(janela = Screen):
    janela.title('Créditos')
    janela.bgpic('fundos/end3.gif')
    time.sleep(2)

def debora_animacao(janela = Screen):
    janela.title('Débora Animações')
    janela.bgpic('fundos/debby.gif')
    janela.exitonclick()

def principal():
    janela = Screen()
    janela.setup(800,600)
    janela.title('Digimon, digitais, Digimon são campeões!')
    janela.bgcolor('white')
    carregaimagens('personagens', janela)
    carregaimagens ('digimons', janela)
    carregaimagens('digimonftowners', janela)
    carregaimagens('fundos', janela)
    cria_personagens()
    abertura(janela)
    ato2(janela)
    ato3(janela)
    ato4(janela)
    ato5(janela)
    ato6(janela)
    ato7(janela)
    ato8(janela)
    #finale(janela)
    fechamento(janela)
    debora_animacao(janela)
       

if __name__=='__main__':
    principal()
    


