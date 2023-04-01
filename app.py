def maximo(c1,c2,cima,esquerdo,diagonal):
    if(c1 == c2 and (diagonal+1) >= cima and (diagonal+1) >= esquerdo):
        diagonal = diagonal+1
        return diagonal
    elif (esquerdo >= cima and esquerdo >= diagonal):
        return esquerdo
    else:
        return cima
    
def ponteiro(c1, c2, cima, esquerdo, diagonal):
    if (c1 == c2 and (diagonal+1) >= cima and (diagonal+1) >= esquerdo):
        return '\\'
    elif (esquerdo >= cima and esquerdo >= diagonal):
        return '_'
    else:
        return '|'
    
def imprimeMatriz(v, w, pontuacao, ponteiros):
    print('\t', end='');
    for j in range(0, len(v)):
        print(v[j], end='\t')
    print()
    for i in range(0, len(w)):
        print(w[i], end='\t')
        for j in range(0, len(v)):
            print(pontuacao[i][j], ponteiros[i][j], end='\t', sep='')
        print()
    print()    

def geraAlinhamento(v, w, pontuacao, ponteiros):
    ali_v =''
    ali_w =''
    i = len(w)-1
    j = len(v)-1
    while ((i!=0) or (j!=0)):
        if (ponteiros[i][j] == '\\'):
            ali_v = v[j] + ali_v
            ali_w = w[i] + ali_w
            i-=1
            j-=1
        elif (ponteiros[i][j] == '_'):
            ali_v = v[j] + ali_v
            ali_w = '_' + ali_w
            j-=1
        else:
            ali_v = '_' + ali_v
            ali_w = w[i] + ali_w
            i-=1
    print(pontuacao[len(w)-1][len(v)-1])
    print(ali_v)
    print(ali_w)

def lcs(v,w):
    pontuacao = []
    ponteiros = []
    pontuacao = [0]*len(v)
    ponteiros = ['']*len(v)

    #inicializa matriz de pontos e ponteiros com zeros e espaços
    for i in range (0, len(w)):
        pontuacao[i] = [0]*len(v)
        ponteiros[i] = ['']*len(v)

    #inicializa a primeira coluna da matriz com barras
    for i in range (0, len(w)):
        ponteiros[i][0] = '|'

    #inicializa a primeira linha da matriz com underscore
    for j in range (0, len(v)):
        ponteiros[0][j] = '_'


    for i in range (1, len(w)): # i = linha 
        for j in range (1, len(v)): #j = coluna
            cima = pontuacao[i-1][j]
            esquerdo = pontuacao[i][j-1]
            diagonal = pontuacao[i-1][j-1]
            c1 = v[j]
            c2 = w[i]
            pontuacao[i][j] = maximo(c1,c2, cima, esquerdo, diagonal)
            ponteiros[i][j] = ponteiro(c1,c2, cima, esquerdo, diagonal)

    imprimeMatriz(v, w, pontuacao, ponteiros)
    geraAlinhamento(v, w, pontuacao, ponteiros)
        
#PROGRAMA PRINCIPAL:
# v = ['*', 'A', 'T', 'C', 'G', 'T', 'A', 'C']
# w = ['*', 'A', 'T', 'G', 'T', 'T', 'A', 'T']

v = ['*', 'D', 'R', 'Q']
w = ['*', 'D', 'R', 'Q']

# v = ['*', "D","R","Q","T","A","Q","A","A","G","T","T","T","I","T"]
# w = ['*', "D","R","N","T","A","Q","L","L","G","T","D","T","T"]
lcs (v,w)  
