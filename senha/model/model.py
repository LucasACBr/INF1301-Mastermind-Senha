import random
import copy

global s, e

def geraSenha(qntdPedras, qntdCores, cores):
    global senha
    senha = []
    for i in range(qntdPedras):
      index = random.randint(0, qntdCores - 1)
      senha.append(cores[index])

    return senha
  
def compara(s,e):
    resultado = []
    senha = copy.copy(s)
    entrada = copy.copy(e)

    for index in range(len(senha)):
      if senha[index] == entrada[index]:
        senha[index] = None
        entrada[index] = None
        resultado.append(1)

    for index in range(len(senha)):
      if entrada[index] != None:
        if entrada[index] in senha:
          indexSenha = senha.index(entrada[index])
          senha[indexSenha] = None
          resultado.append(0)
        else:
          resultado.append(-1)
    
    return resultado

        

def jogada(contador, qntdPedras, senha, lista):
    resultado=[]
    if (contador >= 0):


      # compara o resultado com a senha
       resultado = compara(senha, lista)
       random.shuffle(resultado)
       print("Resultado",resultado)

      #verifica se o usuário venceu
      #if resultado == validador:
         # print("Parabéns, você ganhou!")
          #venceu = True
          
      #if contador == 0:
           #print("Você perdeu!")
      #else:            
      # random.shuffle(resultado)
       #print("Resultado",resultado)


      
    return resultado

def verificaVenceu(resultado,contador,nCoresSelecionadas,qntdPedras):
    nCertos=0
    for i in range(len(resultado)):
        if resultado[i] != 1:
                if (contador==0):
                    print("Você perdeu!")
                    venceu = 0
                    return venceu
        elif (resultado[i] == 1):
            nCertos=nCertos+1
            print("olha certo",nCertos)
            if (nCertos==qntdPedras):
                print("Parabéns, você ganhou!")
                venceu = 1
                return venceu
    venceu = -2    
    return venceu

