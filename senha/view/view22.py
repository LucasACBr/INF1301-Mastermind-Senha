from tkinter import *
import random
from functools import partial
from view import view
from model import model




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


global d_Pedras, t_Pedras ,x_PedrasOG,x_Pedras,y_Pedras, dH_Botoes , h_inicialB1,h_inicialB2,h_atualB1,h_atualB2,d_jogadas,h_inicialJ1 ,h_inicialJ2,qntdPedras, qntdCores, contador,senha,j, contador_string,jr,nivel, colors
colors = ["#FF0000", "#FF8000", "#FFFF00", "#00FF00", "#000099", "#9933FF","#FF99FF", "#00FFFF"]
jr=0
d_Pedras = 80
t_Pedras = 30
x_PedrasOG = 0
x_Pedras = 0
y_Pedras = 0
dH_Botoes = 80
h_inicialB1 = 20
h_inicialB2 = 50
h_atualB1=0
h_atualB2=0
d_jogadas = 50
h_inicialJ1 = 20
h_inicialJ2 = 90
contador_string = 0
nivel=0
global qntdPedras ,qntdCores,contador,senha ,nCoresSelecionadas,nJogadas,root, canvas,flag,entrada,listaDeJogadas
qntdPedras=0
qntdCores=0
contador=0
senha=0
nCoresSelecionadas = 0
nJogadas=0
flag=0
entrada = []
listaDeJogadas=[]

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle
    


def escolheDificuldade(nivel):
    colors = ["#FF0000", "#FF8000", "#FFFF00", "#00FF00", "#000099", "#9933FF","#FF99FF", "#00FFFF"]
    global qntdPedras ,qntdCores,contador,senha,h_inicialJ1,h_inicialJ2,nJogadas,x_Pedras,x_PedrasOG,nCoresSelecionadas,flag
    
    if nivel == 1:
      qntdPedras = 4
      qntdCores = 6
      contador = 8
      flag=1

    elif nivel == 2:
      qntdPedras = 5
      qntdCores = 7
      contador = 10
      flag=1

    else:
      qntdPedras = 6
      qntdCores = 8
      contador = 12
      flag=1
      
    h_inicialJ1 = 25 + d_jogadas
    h_inicialJ2 = 25 + 2*d_jogadas
    nJogadas=0
    x_PedrasOG = 100 + d_jogadas
    x_Pedras = x_PedrasOG #retornar x_Pedras para x_PedrasOG apos jogada
    nCoresSelecionadas=0
    senha = funcoesLogicaSenha.geraSenha(qntdPedras, qntdCores, colors)
    montarTabuleiro(contador)
    return




def botoes():
    h_atualB1= dH_Botoes + h_inicialB1
    h_atualB2= dH_Botoes + h_inicialB2

    #cor de fundo do tabuleiro
    canvas.create_rectangle(850, 700, 0, 0, outline="black", fill="purple", width=3)

    # Cria botão Nível I
    comando_1 = partial(escolheDificuldade, 1)#importar para controller
    h_atualB1= dH_Botoes + h_atualB1
    h_atualB2= dH_Botoes + h_atualB2
    Nivel_I = Button(canvas, font="Helvetica 18 bold",bd=4,text="Nível I", command =comando_1, width=15)
    Nivel_I.place(x=910, y=((h_atualB2)+(h_atualB1))/2)

    # Cria botão Nível II
    comando_2 = partial(escolheDificuldade, 2)#importar para controller
    h_atualB1 = dH_Botoes + h_atualB1
    h_atualB2 = dH_Botoes + h_atualB2
    Nivel_II = Button(canvas, font="Helvetica 18 bold",bd=4,text="Nível II", command = comando_2, width=15)
    Nivel_II.place(x=910, y=((h_atualB2)+(h_atualB1))/2)

    # Cria botão Nível III
    comando_3 = partial(escolheDificuldade, 3)#importar para controller
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
    canvas.bind('<Button>', move)
    canvas.mainloop()
    return 

def montaTabelaJogadas():
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




def montaCanvasJogadasUsuario():
    global nJogadas
    global h_inicialJ1
    global h_inicialJ2
    if (contador!=0):
        
        x_PedrasOG = 100 + d_jogadas
        x_Pedras = x_PedrasOG #retornar x_Pedras para x_PedrasOG apos jogada

        y_Pedras = (h_inicialJ1 +h_inicialJ2)/2
        #p_Lista = contador lista de pedras
        
        for i in range(qntdPedras):
            #p_Lista[i].append(canvas.create_circle(x_Pedras, y_Pedras, t_Pedras/2, fill="white",outline="black", width=1))
            canvas.create_circle(x_Pedras, y_Pedras+d_jogadas*(nJogadas), t_Pedras/2, fill="white",outline="black", width=1)
            canvas.create_circle(x_Pedras+300, y_Pedras+d_jogadas*(nJogadas), t_Pedras/2, fill="white",outline="black", width=1)
            x_Pedras = x_Pedras + d_Pedras/2
        return


def montaDicas():
    global nJogadas
    global h_inicialJ1
    global h_inicialJ2
    if (contador!=0):
        
        x_PedrasOG = 100 + d_jogadas
        x_Pedras = x_PedrasOG #retornar x_Pedras para x_PedrasOG apos jogada

        y_Pedras = (h_inicialJ1 +h_inicialJ2)/2
        #p_Lista = contador lista de pedras
        
        for i in range(qntdPedras):
            #p_Lista[i].append(canvas.create_circle(x_Pedras, y_Pedras, t_Pedras/2, fill="white",outline="black", width=1))
            canvas.create_circle(x_Pedras+300, y_Pedras+d_jogadas*(nJogadas), t_Pedras/2, fill="white",outline="black", width=1)
            x_Pedras = x_Pedras + d_Pedras/2
        return
    

def montaPaletaCores():
    j = 0
    lstPaleta=[]
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
    canvas.create_rectangle(575, 20, 280, 70, outline="black", fill="white", width=3)
    canvas.create_text(300, 45, anchor=W, font="Helvetica 18 bold",text="Jogadas restantes: ")
        
    if (qntdPedras == 4):
        jr=canvas.create_text(530, 45, anchor=W, font="Helvetica 18 bold",text="8")
    elif (qntdPedras == 5):
        jr=canvas.create_text(530, 45, anchor=W, font="Helvetica 18 bold",text="10")
    else:
        jr=canvas.create_text(530, 45, anchor=W, font="Helvetica 18 bold",text="12")




def montarTabuleiro(contador):

    montaTabelaJogadas()
    montaCanvasJogadasUsuario()
    montaJogadasRestantes()

    x_Pedras = x_PedrasOG
    y_Pedras = (h_inicialJ1 +h_inicialJ2)/2
    
    montaPaletaCores()

    return


def insereCorTab(contador,i):
        global h_inicialJ1,h_inicialJ2,x_Pedras,entrada,nCoresSelecionadas,listaDeJogadas
        y_Pedras = (h_inicialJ1 +h_inicialJ2)/2
        canvas.create_circle(x_Pedras + nCoresSelecionadas*(d_Pedras/2), y_Pedras+d_jogadas*(nJogadas), t_Pedras/2, fill=colors[i],outline="black", width=1)
        if (nCoresSelecionadas == qntdPedras):
            listaDeJogadas.append(entrada)
            entrada=[]
        else:
            entrada.append(colors[i])
        

def atualizaContador():
    global contador
    global nJogadas
    global x_Pedras
    global x_PedrasOG
    if (contador!=0):
        contador=contador-1
        nJogadas=nJogadas+1
        x_Pedras=x_PedrasOG
        contador_string=str(contador)
        canvas.itemconfigure(jr, text=contador_string)

    


def verificaJogadas():
    global nCoresSelecionadas
    global contador
    if (contador!=0):
        if (nCoresSelecionadas == qntdPedras):
            nCoresSelecionadas=0
            atualizaContador()
            montaCanvasJogadasUsuario()
            
            return nCoresSelecionadas
        else:
            return nCoresSelecionadas

    

def move(event):
    xInicialMin=870
    xInicialMax=930
    yInicialMin=545
    yInicialMax=605
    xMin=xInicialMin
    xMax=xInicialMax
    global nCoresSelecionadas
    if (contador!=0):
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>yInicialMin and (event.y)<yInicialMax):
                #mover primeira cor
                i=0
                insereCorTab(contador,i)
                nCoresSelecionadas=nCoresSelecionadas+1
                nCoresSelecionadas=verificaJogadas()
                
        xMin=80 + xInicialMin
        xMax=80 + xInicialMax
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>yInicialMin and (event.y)<yInicialMax):
                #mover segunda cor
                i=1
                insereCorTab(contador,i)
                nCoresSelecionadas=nCoresSelecionadas+1
                nCoresSelecionadas=verificaJogadas()
                
        xMin=80 + xMin
        xMax=80 + xMax
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>yInicialMin and (event.y)<yInicialMax):
                #mover terceira cor
                i=2
                insereCorTab(contador,i)
                nCoresSelecionadas=nCoresSelecionadas+1
                nCoresSelecionadas=verificaJogadas()
                
        xMin=80 + xMin
        xMax=80 + xMax  
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>yInicialMin and (event.y)<yInicialMax):
                #mover quarta cor
                i=3
                insereCorTab(contador,i)
                nCoresSelecionadas=nCoresSelecionadas+1
                nCoresSelecionadas=verificaJogadas()

        xMin=xInicialMin
        xMax=xInicialMax
        
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>620 and (event.y)<680):
                #mover quinta cor
                i=4
                insereCorTab(contador,i)
                nCoresSelecionadas=nCoresSelecionadas+1
                nCoresSelecionadas=verificaJogadas()

        xMin=80 + xMin
        xMax=80 + xMax  
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>620 and (event.y)<680):
                #mover sexta cor
                i=5
                insereCorTab(contador,i)
                nCoresSelecionadas=nCoresSelecionadas+1
                nCoresSelecionadas=verificaJogadas()
                
        xMin=80 + xMin
        xMax=80 + xMax  
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>620 and (event.y)<680):
                #mover setima cor
                i=6
                insereCorTab(contador,i)
                nCoresSelecionadas=nCoresSelecionadas+1
                nCoresSelecionadas=verificaJogadas()
                
        xMin=80 + xMin
        xMax=80 + xMax  
        if ((event.x)>xMin and (event.x)<xMax):
            if ((event.y)>620 and (event.y)<680):
                #mover oitava cor
                i=7
                insereCorTab(contador,i)
                nCoresSelecionadas=nCoresSelecionadas+1
                nCoresSelecionadas=verificaJogadas()


def retFlag():
    global flag
    return flag

def retSenha():
    global senha
    return senha

def retContador():
    global contador
    return contador

def retQntdPedras():
    global qntdPedras
    return qntdPedras

def retEntrada():
    global entrada
    return entrada

def retnCoresSelecionadas():
    global nCoresSelecionadas
    return nCoresSelecionadas

#Início de Fato da Partida

