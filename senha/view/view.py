from tkinter import *
import random
from functools import partial
from model import model
from controller import controller


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
global d_Pedras,d_jogadas,dH_Botoes, t_Pedras ,x_PedrasOG,x_Pedras,y_Pedras,h_inicialB1,h_inicialB2,h_atualB1,h_atualB2,h_inicialJ1 ,h_inicialJ2
d_Pedras = 80
d_jogadas = 50
dH_Botoes = 80
t_Pedras = 30
x_PedrasOG = 0
x_Pedras = 0
y_Pedras = 0
h_inicialB1 = 20
h_inicialB2 = 50
h_atualB1=0
h_atualB2=0
h_inicialJ1 = 20
h_inicialJ2 = 90

#Globais variaveis para armazenamento de informacao
global qntdPedras ,qntdCores,contador,senha ,nCoresSelecionadas,nJogadas,flag,nivel,contador_string,jr,entrada,listaDeJogadas,j,canvas,root,nCirculosResultados,venceu
qntdPedras=0
qntdCores=0
contador=0
senha=0
nCoresSelecionadas = 0
nJogadas=0
flag=0
nivel=0
contador_string = 0
jr=0
entrada = []
listaDeJogadas=[]
nCirculosResultados=0
venceu=-2
#funcao para facilitar criacao de circulos
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle


def escolheDificuldade(nivel):
    colors = ["#FF0000", "#FF8000", "#FFFF00", "#00FF00", "#000099", "#9933FF","#FF99FF", "#00FFFF"]
    global qntdPedras ,qntdCores,contador,senha,h_inicialJ1,h_inicialJ2,nJogadas,x_Pedras,x_PedrasOG,nCoresSelecionadas,venceu
    
    if nivel == 1:
      qntdPedras = 4
      qntdCores = 6
      contador = 8

    elif nivel == 2:
      qntdPedras = 5
      qntdCores = 7
      contador = 10
      
    else:
      qntdPedras = 6
      qntdCores = 8
      contador = 12

    venceu=-2
    h_inicialJ1 = 25 + d_jogadas
    h_inicialJ2 = 25 + 2*d_jogadas
    nJogadas=0
    x_PedrasOG = 100 + d_jogadas
    x_Pedras = x_PedrasOG #retornar x_Pedras para x_PedrasOG apos jogada
    nCoresSelecionadas=0
    senha = model.geraSenha(qntdPedras, qntdCores, colors)
    montarTabuleiro()
    return

def inicializa():
    #inicia canvas
    global root, canvas
    root = Tk()
    root.wm_title("Mastermind:Senha")
    canvas = Canvas(root, width=1200, height=700, borderwidth=0, highlightthickness=0, bg="white")
    canvas.grid()
    #interface grafica inicial
    canvas.create_rectangle(1200, 700, 850, 0, outline="black", fill="grey", width=3)
    canvas.create_text(870, 55, anchor=W, font="Helvetica 26 bold",text="Mastermind:Senha")
    canvas.create_text(935, (dH_Botoes + h_inicialB2), anchor=W, font="Helvetica 22 bold",text="Nova Partida:")
    canvas.create_rectangle(1200, 700, 850, 530, fill="grey", width=3)
    botoes()
    canvas.mainloop()
    return 

def criaImagemVenceu(resultado,contador,nCoresSelecionadas,qntdPedras):
    global venceu,root, canvas
    venceu=model.verificaVenceu(resultado,contador,nCoresSelecionadas,qntdPedras)
    if (venceu == 1):
        canvas.create_text(420, 45, anchor=W, font="Helvetica 18 bold",text="Parabéns você Venceu!")
    elif (venceu == 0):
        canvas.create_text(470, 45, anchor=W, font="Helvetica 18 bold",text="Você Perdeu!")


def montaTabelaJogadas():
    global canvas
    # Cor de fundo do tabuleiro
    canvas.create_rectangle(850, 700, 0, 0, outline="black", fill="purple", width=3)
    # Monta Tabela com as Jogadas
    h_inicialJ1 = 25 + d_jogadas
    h_inicialJ2 = 25 + 2*d_jogadas
    
    for i in range(contador):
        canvas.create_rectangle(400, h_inicialJ1, 100, h_inicialJ2, outline="black", fill="white", width=2)
        canvas.create_rectangle(700, h_inicialJ1, 400, h_inicialJ2, outline="black", fill="white", width=2)
        h_inicialJ1 += d_jogadas
        h_inicialJ2 += d_jogadas
    return


def botoes():
    canvas.bind('<Button>', controller.move)
    h_atualB1= dH_Botoes + h_inicialB1
    h_atualB2= dH_Botoes + h_inicialB2

    #cor de fundo do tabuleiro
    canvas.create_rectangle(850, 700, 0, 0, outline="black", fill="purple", width=3)

    # Cria botão Nível I
    comando_1 = partial(escolheDificuldade, 1)
    h_atualB1= dH_Botoes + h_atualB1
    h_atualB2= dH_Botoes + h_atualB2
    Nivel_I = Button(canvas, font="Helvetica 18 bold",bd=4,text="Nível I", command =comando_1, width=15)
    Nivel_I.place(x=910, y=((h_atualB2)+(h_atualB1))/2)

    # Cria botão Nível II
    comando_2 = partial(escolheDificuldade, 2)
    h_atualB1 = dH_Botoes + h_atualB1
    h_atualB2 = dH_Botoes + h_atualB2
    Nivel_II = Button(canvas, font="Helvetica 18 bold",bd=4,text="Nível II", command = comando_2, width=15)
    Nivel_II.place(x=910, y=((h_atualB2)+(h_atualB1))/2)

    # Cria botão Nível III
    comando_3 = partial(escolheDificuldade, 3)
    h_atualB1 = dH_Botoes + h_atualB1
    h_atualB2 = dH_Botoes + h_atualB2
    Nivel_III = Button(canvas, font="Helvetica 18 bold",bd=4,text="Nível III", command =comando_3, width=15)
    Nivel_III.place(x=910, y=((h_atualB2)+(h_atualB1))/2)
    
    # Cria botão Iniciar Partida
    h_atualB1 = dH_Botoes + h_atualB1
    h_atualB2 = dH_Botoes + h_atualB2
    continuarP = Button(canvas, font="Helvetica 18 bold",bd=4,text="Continuar Partida", command = lambda: print("em tese continua partida"), width=15)
    continuarP.place(x=910, y=((h_atualB2)+(h_atualB1))/2)
    return


def montaCanvasJogadasUsuario():
    global nJogadas
    global h_inicialJ1
    global h_inicialJ2
    global contador
    contador=contador-1   
    if (contador>=0):
        x_PedrasOG = 100 + d_jogadas
        x_Pedras = x_PedrasOG #retornar x_Pedras para x_PedrasOG apos jogada
        y_Pedras = (h_inicialJ1 + h_inicialJ2)/2
        for i in range(qntdPedras):
            canvas.create_circle(x_Pedras, y_Pedras+d_jogadas*(nJogadas), t_Pedras/2, fill="white",outline="black", width=1)
            x_Pedras = x_Pedras + d_Pedras/2
        nJogadas=nJogadas+1
        return


def montaDicas(resultadoDicas):
    global nJogadas
    global h_inicialJ1
    global h_inicialJ2
    global nCirculosResultados
    if (contador>=0):
        
        x_PedrasOG = 100 + d_jogadas
        x_Pedras = x_PedrasOG
        y_Pedras = (h_inicialJ1 +h_inicialJ2)/2

        #-1 represeta erro total de cor e posicao
        #0 represeta erro de posicao porem acertou a cor
        #1 representa acertar a cor e posicao
        for i in range(len(resultadoDicas)):
            if (resultadoDicas[i]==1):
                 canvas.create_circle(x_Pedras+300, y_Pedras+d_jogadas*(nJogadas-1), t_Pedras/2, fill="black",outline="black", width=1)
                 nCirculosResultados=nCirculosResultados+1
                 x_Pedras = x_Pedras + d_Pedras/2
            elif (resultadoDicas[i]==0):
                canvas.create_circle(x_Pedras+300, y_Pedras+d_jogadas*(nJogadas-1), t_Pedras/2, fill="white",outline="black", width=1)
                nCirculosResultados=nCirculosResultados+1
                x_Pedras = x_Pedras + d_Pedras/2

    return
    

def montaPaletaCores():
    j = 0
    canvas.create_rectangle(1200, 700, 850, 530, fill="grey", width=3)
    for i in range(qntdCores):
        if(i<4):
            (canvas.create_circle(900+(d_Pedras)*(i), 575, t_Pedras, fill=colors[i], outline="black", width=1))
        else:
            (canvas.create_circle(900+(d_Pedras)*(j), 650, t_Pedras, fill=colors[i], outline="black", width=1))
            j=j+1

def montaJogadasRestantes():
    global jr
    # Monta Box com Jogadas Restantes
    canvas.create_rectangle(380, 20, 100, 70, outline="black", fill="white", width=3)
    canvas.create_text(110, 45, anchor=W, font="Helvetica 18 bold",text="Jogadas restantes: ")
    # Monta Box com Resultado Venceu
    canvas.create_rectangle(700, 20, 400, 70, outline="black", fill="white", width=3)
        
    if (qntdPedras == 4):
        jr=canvas.create_text(330, 45, anchor=W, font="Helvetica 18 bold",text="8")
    elif (qntdPedras == 5):
        jr=canvas.create_text(330, 45, anchor=W, font="Helvetica 18 bold",text="10")
    else:
        jr=canvas.create_text(330, 45, anchor=W, font="Helvetica 18 bold",text="12")


def atualizaContadorVisual(contador):
    contador_string=str(contador)
    canvas.itemconfigure(jr, text=contador_string)

def atualizaNCoresSelecionadas():
    global nCoresSelecionadas
    global contador
    global qntdPedras
    nCoresSelecionadas=nCoresSelecionadas+1
    nCoresSelecionadas=controller.verificaJogadas(nCoresSelecionadas)
    
    return nCoresSelecionadas

def montarTabuleiro():

    montaTabelaJogadas()
    montaCanvasJogadasUsuario()
    montaJogadasRestantes()

    x_Pedras = x_PedrasOG
    y_Pedras = (h_inicialJ1 +h_inicialJ2)/2
    
    montaPaletaCores()

    return

def retCanvas():
    global canvas
    return canvas

def retSenha():
    global senha
    return senha

def retContador():
    global contador
    return contador

def retQntdPedras():
    global qntdPedras
    return qntdPedras

def ret_x_Pedras():
    global x_Pedras
    return x_Pedras

def ret_y_Pedras():
    global y_Pedras
    return y_Pedras

def ret_Venceu():
    global venceu
    return venceu

def ret_nJogadas():
    global nJogadas
    return nJogadas

def ret_nCoresSelecionadas():
    global nCoresSelecionadas
    return nCoresSelecionadas

def ret_Senha():
    global senha
    return senha
#Início de Fato da Partida

