ç = " "
validos = ["X", "O"]

def Fazvelha(): 
    jogo = [
    [ç,ç,ç],
    [ç,ç,ç],
    [ç,ç,ç]
]
    return jogo

#Cria o formato do jogo da velha
def Criadesenho(jogo):
    for i in range(3):
        print("|". join(jogo[i]))
 
#valida se o numero inserido corresponde a uma posição da tabela
def validação(men):
    try:
        n = int(input(men))
        if(n >= 1 and n <=3):
            return n - 1
        else:
            print("invalido")
            return validação(men)
    except:
        print("numero invalido")
        return validação(men)
    
#verifica se há uma sequencia de mesmo simbolo em uma diagonal, vertical ou na diagonal       
def verificaGanhador(jogo):
    # verifica as linhas
    for i in range(3):
        if jogo[i][0] == jogo[i][1] and jogo[i][1] == jogo[i][2] and jogo[i][0] != ç:
            return jogo[i][0]
    
     # verifica as colunas
    for i in range(3):
        if jogo[0][i] == jogo[1][i] and jogo[1][i] == jogo[2][i] and jogo[0][i] != ç:
            return jogo[0][i]
    
     # verifica a diagonal principal
    if jogo[0][0] == jogo[1][1] and jogo[1][1] == jogo[2][2] and jogo[0][0] != ç:
        return jogo[0][0]
    
     # verifica a diagonal secundaria
    if jogo[0][2] == jogo[1][1] and jogo[1][1] == jogo[2][0] and jogo[0][2] != ç:
        return jogo[0][0]
    
    #verifica se nem uma casa esta em branco
    for l in range(3):
        for c in range(3):
            if jogo[l][c] == ç:
                return False
            
    return "deu velha"

#verifica se a posição escolhida ja foi preenchida
def verificaJogada(jogo , l, c):
    if jogo[l][c] == ç:
        return True
    else:
        return False

#substitui "" por X ou O
def jogada(jogo , l, c, jogador):
    jogo[l][c] = validos[jogador]
        
jogador = 0
jogo = Fazvelha()
ganhador = verificaGanhador(jogo)
 

while(not ganhador):
    Criadesenho(jogo)
    print("numeros de 1  a 3")
    l = validação("digite a linha: ")
    c = validação("digite a coluna: ")
    
    if (verificaJogada(jogo , l, c)):
        jogada(jogo , l, c, jogador)
        jogador = (jogador + 1)%2 #altera entre o jogador 0(X) e o jogador 1(O)
    else:
        print("ja esta ocupada")
        
    ganhador = verificaGanhador(jogo)

   
print("____________________________________________")
print("")
Criadesenho(jogo)
print("GANHADOR: ", ganhador)
print("____________________________________________")
    
     