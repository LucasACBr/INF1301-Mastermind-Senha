from tkinter import *
import random
from functools import partial
from model import model
from view import view
import copy

global colors
colors = ["#FF0000", "#FF8000", "#FFFF00", "#00FF00", "#000099", "#9933FF","#FF99FF", "#00FFFF"]
#canvasT = Canvas(root, width=1200, height=700, borderwidth=0, highlightthickness=0, bg="white")
#canvasB.grid()
#canvasT.grid()
#LEGENDA CORES
#FF8000 = LARANJA
#00FF00 = VERDE
#000099 = AZUL ESCURO
#9933FF = ROXO
#FF0000 = VERMELHO
#FFFF00 = AMARELO
#FF99FF = ROSA
#00FFFF = AZUL CLARO

#Globais variaveis de manipulacao de coordenadas
global d_Pedras,d_jogadas,t_Pedras ,x_PedrasOG,x_Pedras,y_Pedras,d_jogadas,h_inicialJ1 ,h_inicialJ2
d_Pedras = 80
d_jogadas = 50
t_Pedras = 30
x_PedrasOG = 0
x_Pedras = 0
y_Pedras = 0
h_inicialJ1 = 20
h_inicialJ2 = 90

#Globais variaveis para armazenamento de informacao
global qntdPedras ,qntdCores,contador,senha ,nCoresSelecionadas,nJogadas,flag,ntrada,listaDeJogadas,canvas,resultado,listaDeResultados,venceu
qntdPedras=0
qntdCores=0
contador=0
senha=0
nCoresSelecionadas = 0
nJogadas=0
flag=0
entrada = []
listaDeJogadas=[]
listaDeResultados=[]
resultado=0
venceu=-2

def manipulaListaDeResultados(resultado):
        listaDeResultados.append(resultado)
        return listaDeJogadas

def manipulaListaDeJogadas(entrada):
        listaDeJogadas.append(entrada)
        return listaDeJogadas


def manipulaEntrada(corInserida,nCoresSelecionadas,qntdPedras):
        global entrada
        global contador
        global senha
        
        senha=view.ret_Senha()
        print("senhaAqui",senha)
        
        contador = view.retContador()
        print("nCoresSelecionadas",nCoresSelecionadas)
        if (nCoresSelecionadas+1>=qntdPedras):
                entrada.append(corInserida)
                print(contador)
                salvaEntrada = copy.copy(entrada)
                resultado=model.jogada(contador, qntdPedras, senha, salvaEntrada)
                salvaResultado = copy.copy(resultado)
                print(salvaResultado)
                salvaResultado2 = copy.copy(resultado)
                salvaResultado3 = copy.copy(resultado)
                view.montaDicas(salvaResultado)
                manipulaListaDeResultados(salvaResultado2)
                view.criaImagemVenceu(salvaResultado3,contador,nCoresSelecionadas,qntdPedras)
                manipulaListaDeJogadas(entrada)
                entrada=[]
        else:
                entrada.append(corInserida)
        return entrada
        


def insereCorTab(contador,i):
        global h_inicialJ1,h_inicialJ2,x_Pedras,entrada,listaDeJogadas,d_jogadas,nCoresSelecionadas
        global canvas
        global nJogadas
        global qntdPedras
        global venceu
        
        qntdPedras=view.retQntdPedras()
        
        if (contador>=0):
                
                nJogadas=view.ret_nJogadas()-1
                nCoresSelecionadas=view.ret_nCoresSelecionadas()
                canvas = view.retCanvas()
                x_PedrasOG = 100 + d_jogadas
                x_Pedras = x_PedrasOG #retornar x_Pedras para x_PedrasOG apos jogada
                y_Pedras = (h_inicialJ1 + h_inicialJ2-10)/2
                y_Pedras=y_Pedras+d_jogadas

                canvas.create_circle(x_Pedras + nCoresSelecionadas*(d_Pedras/2), y_Pedras+d_jogadas*(nJogadas), t_Pedras/2, fill=colors[i],outline="black", width=1)
                manipulaEntrada(colors[i],nCoresSelecionadas,qntdPedras)
                    
        

def atualizaContador(contador):
    global nCoresSelecionadas
    global nJogadas
    global x_Pedras
    global x_PedrasOG
    global canvas
    
    nCoresSelecionadas=view.atualizaNCoresSelecionadas()
    
    if (nCoresSelecionadas==0):
        x_Pedras=x_PedrasOG
        view.atualizaContadorVisual(contador)

    return nCoresSelecionadas
                


def verificaJogadas(nCoresSelecionadas):
    global contador
    global qntdPedras
    
    qntdPedras=view.retQntdPedras()
    
    if (contador>=0):
        
        if (nCoresSelecionadas == qntdPedras):
            nCoresSelecionadas=0
            view.montaCanvasJogadasUsuario()
        
            return nCoresSelecionadas
        
        else:
            
            return nCoresSelecionadas
    

def move(event):
    global nCoresSelecionadas
    global contador
    global canvas
    global qntdPedras
    global venceu
    
    canvas = view.retCanvas()
    contador = view.retContador()
    qntdPedras = view.retQntdPedras()
    venceu=view.ret_Venceu()
    
    xInicialMin=870
    xInicialMax=930
    yInicialMin=545
    yInicialMax=605
    xMin=xInicialMin
    xMax=xInicialMax
    
    if (contador>=0 and venceu==-2):
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>yInicialMin and (event.y)<yInicialMax):
                #mover primeira cor
                i=0
                insereCorTab(contador,i)
                nCoresSelecionadas=atualizaContador(contador)
                
        xMin=80 + xInicialMin
        xMax=80 + xInicialMax
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>yInicialMin and (event.y)<yInicialMax):
                #mover segunda cor
                i=1
                insereCorTab(contador,i)
                nCoresSelecionadas=atualizaContador(contador)
                
        xMin=80 + xMin
        xMax=80 + xMax
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>yInicialMin and (event.y)<yInicialMax):
                #mover terceira cor
                i=2
                insereCorTab(contador,i)
                nCoresSelecionadas=atualizaContador(contador)
                
        xMin=80 + xMin
        xMax=80 + xMax  
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>yInicialMin and (event.y)<yInicialMax):
                #mover quarta cor
                i=3
                insereCorTab(contador,i)
                nCoresSelecionadas=atualizaContador(contador)

        xMin=xInicialMin
        xMax=xInicialMax
        
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>620 and (event.y)<680):
                #mover quinta cor
                i=4
                insereCorTab(contador,i)
                nCoresSelecionadas=atualizaContador(contador)

        xMin=80 + xMin
        xMax=80 + xMax  
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>620 and (event.y)<680):
                #mover sexta cor
                i=5
                insereCorTab(contador,i)
                nCoresSelecionadas=atualizaContador(contador)
                
        if(qntdPedras>4):
            xMin=80 + xMin
            xMax=80 + xMax  
            if ((event.x)>xMin and (event.x)<xMax):
                if ((event.y)>620 and (event.y)<680):
                    #mover setima cor
                    i=6
                    insereCorTab(contador,i)
                    nCoresSelecionadas=atualizaContador(contador)
                    
            if(qntdPedras>5):
                xMin=80 + xMin
                xMax=80 + xMax  
                if ((event.x)>xMin and (event.x)<xMax):
                    if ((event.y)>620 and (event.y)<680):
                        #mover oitava cor
                        i=7
                        insereCorTab(contador,i)
                        nCoresSelecionadas=atualizaContador(contador)


def retFlag():
    global flag
    return flag

def retListaDeJogadas():
    global listaDeJogadas
    return listaDeJogadas

def retEntrada():
    global entrada
    return entrada

def retnCoresSelecionadas():
    global nCoresSelecionadas
    return nCoresSelecionadas


def ret_contadorController():
    global contadorController
    return contadorController


#Início de Fato da Partida

