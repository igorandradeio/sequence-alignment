AMINOACID_CODES = [
    "A",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "V",
    "W",
    "Y",
]

BLOSUM62 = {
    ("W", "F"): 1,
    ("L", "R"): -2,
    ("S", "P"): -1,
    ("V", "T"): 0,
    ("Q", "Q"): 5,
    ("N", "A"): -2,
    ("Z", "Y"): -2,
    ("W", "R"): -3,
    ("Q", "A"): -1,
    ("S", "D"): 0,
    ("H", "H"): 8,
    ("S", "H"): -1,
    ("H", "D"): -1,
    ("L", "N"): -3,
    ("W", "A"): -3,
    ("Y", "M"): -1,
    ("G", "R"): -2,
    ("Y", "I"): -1,
    ("Y", "E"): -2,
    ("B", "Y"): -3,
    ("Y", "A"): -2,
    ("V", "D"): -3,
    ("B", "S"): 0,
    ("Y", "Y"): 7,
    ("G", "N"): 0,
    ("E", "C"): -4,
    ("Y", "Q"): -1,
    ("Z", "Z"): 4,
    ("V", "A"): 0,
    ("C", "C"): 9,
    ("M", "R"): -1,
    ("V", "E"): -2,
    ("T", "N"): 0,
    ("P", "P"): 7,
    ("V", "I"): 3,
    ("V", "S"): -2,
    ("Z", "P"): -1,
    ("V", "M"): 1,
    ("T", "F"): -2,
    ("V", "Q"): -2,
    ("K", "K"): 5,
    ("P", "D"): -1,
    ("I", "H"): -3,
    ("I", "D"): -3,
    ("T", "R"): -1,
    ("P", "L"): -3,
    ("K", "G"): -2,
    ("M", "N"): -2,
    ("P", "H"): -2,
    ("F", "Q"): -3,
    ("Z", "G"): -2,
    ("X", "L"): -1,
    ("T", "M"): -1,
    ("Z", "C"): -3,
    ("X", "H"): -1,
    ("D", "R"): -2,
    ("B", "W"): -4,
    ("X", "D"): -1,
    ("Z", "K"): 1,
    ("F", "A"): -2,
    ("Z", "W"): -3,
    ("F", "E"): -3,
    ("D", "N"): 1,
    ("B", "K"): 0,
    ("X", "X"): -1,
    ("F", "I"): 0,
    ("B", "G"): -1,
    ("X", "T"): 0,
    ("F", "M"): 0,
    ("B", "C"): -3,
    ("Z", "I"): -3,
    ("Z", "V"): -2,
    ("S", "S"): 4,
    ("L", "Q"): -2,
    ("W", "E"): -3,
    ("Q", "R"): 1,
    ("N", "N"): 6,
    ("W", "M"): -1,
    ("Q", "C"): -3,
    ("W", "I"): -3,
    ("S", "C"): -1,
    ("L", "A"): -1,
    ("S", "G"): 0,
    ("L", "E"): -3,
    ("W", "Q"): -2,
    ("H", "G"): -2,
    ("S", "K"): 0,
    ("Q", "N"): 0,
    ("N", "R"): 0,
    ("H", "C"): -3,
    ("Y", "N"): -2,
    ("G", "Q"): -2,
    ("Y", "F"): 3,
    ("C", "A"): 0,
    ("V", "L"): 1,
    ("G", "E"): -2,
    ("G", "A"): 0,
    ("K", "R"): 2,
    ("E", "D"): 2,
    ("Y", "R"): -2,
    ("M", "Q"): 0,
    ("T", "I"): -1,
    ("C", "D"): -3,
    ("V", "F"): -1,
    ("T", "A"): 0,
    ("T", "P"): -1,
    ("B", "P"): -2,
    ("T", "E"): -1,
    ("V", "N"): -3,
    ("P", "G"): -2,
    ("M", "A"): -1,
    ("K", "H"): -1,
    ("V", "R"): -3,
    ("P", "C"): -3,
    ("M", "E"): -2,
    ("K", "L"): -2,
    ("V", "V"): 4,
    ("M", "I"): 1,
    ("T", "Q"): -1,
    ("I", "G"): -4,
    ("P", "K"): -1,
    ("M", "M"): 5,
    ("K", "D"): -1,
    ("I", "C"): -1,
    ("Z", "D"): 1,
    ("F", "R"): -3,
    ("X", "K"): -1,
    ("Q", "D"): 0,
    ("X", "G"): -1,
    ("Z", "L"): -3,
    ("X", "C"): -2,
    ("Z", "H"): 0,
    ("B", "L"): -4,
    ("B", "H"): 0,
    ("F", "F"): 6,
    ("X", "W"): -2,
    ("B", "D"): 4,
    ("D", "A"): -2,
    ("S", "L"): -2,
    ("X", "S"): 0,
    ("F", "N"): -3,
    ("S", "R"): -1,
    ("W", "D"): -4,
    ("V", "Y"): -1,
    ("W", "L"): -2,
    ("H", "R"): 0,
    ("W", "H"): -2,
    ("H", "N"): 1,
    ("W", "T"): -2,
    ("T", "T"): 5,
    ("S", "F"): -2,
    ("W", "P"): -4,
    ("L", "D"): -4,
    ("B", "I"): -3,
    ("L", "H"): -3,
    ("S", "N"): 1,
    ("B", "T"): -1,
    ("L", "L"): 4,
    ("Y", "K"): -2,
    ("E", "Q"): 2,
    ("Y", "G"): -3,
    ("Z", "S"): 0,
    ("Y", "C"): -2,
    ("G", "D"): -1,
    ("B", "V"): -3,
    ("E", "A"): -1,
    ("Y", "W"): 2,
    ("E", "E"): 5,
    ("Y", "S"): -2,
    ("C", "N"): -3,
    ("V", "C"): -1,
    ("T", "H"): -2,
    ("P", "R"): -2,
    ("V", "G"): -3,
    ("T", "L"): -1,
    ("V", "K"): -2,
    ("K", "Q"): 1,
    ("R", "A"): -1,
    ("I", "R"): -3,
    ("T", "D"): -1,
    ("P", "F"): -4,
    ("I", "N"): -3,
    ("K", "I"): -3,
    ("M", "D"): -3,
    ("V", "W"): -3,
    ("W", "W"): 11,
    ("M", "H"): -2,
    ("P", "N"): -2,
    ("K", "A"): -1,
    ("M", "L"): 2,
    ("K", "E"): 1,
    ("Z", "E"): 4,
    ("X", "N"): -1,
    ("Z", "A"): -1,
    ("Z", "M"): -1,
    ("X", "F"): -1,
    ("K", "C"): -3,
    ("B", "Q"): 0,
    ("X", "B"): -1,
    ("B", "M"): -3,
    ("F", "C"): -2,
    ("Z", "Q"): 3,
    ("X", "Z"): -1,
    ("F", "G"): -3,
    ("B", "E"): 1,
    ("X", "V"): -1,
    ("F", "K"): -3,
    ("B", "A"): -2,
    ("X", "R"): -1,
    ("D", "D"): 6,
    ("W", "G"): -2,
    ("Z", "F"): -3,
    ("S", "Q"): 0,
    ("W", "C"): -2,
    ("W", "K"): -3,
    ("H", "Q"): 0,
    ("L", "C"): -1,
    ("W", "N"): -4,
    ("S", "A"): 1,
    ("L", "G"): -4,
    ("W", "S"): -3,
    ("S", "E"): 0,
    ("H", "E"): 0,
    ("S", "I"): -2,
    ("H", "A"): -2,
    ("S", "M"): -1,
    ("Y", "L"): -1,
    ("Y", "H"): 2,
    ("Y", "D"): -3,
    ("E", "R"): 0,
    ("X", "P"): -2,
    ("G", "G"): 6,
    ("G", "C"): -3,
    ("E", "N"): 0,
    ("Y", "T"): -2,
    ("Y", "P"): -3,
    ("T", "K"): -1,
    ("A", "A"): 4,
    ("P", "Q"): -1,
    ("T", "C"): -1,
    ("V", "H"): -3,
    ("T", "G"): -2,
    ("I", "Q"): -3,
    ("Z", "T"): -1,
    ("C", "R"): -3,
    ("V", "P"): -2,
    ("P", "E"): -1,
    ("M", "C"): -1,
    ("K", "N"): 0,
    ("I", "I"): 4,
    ("P", "A"): -1,
    ("M", "G"): -3,
    ("T", "S"): 1,
    ("I", "E"): -3,
    ("P", "M"): -2,
    ("M", "K"): -1,
    ("I", "A"): -1,
    ("P", "I"): -3,
    ("R", "R"): 5,
    ("X", "M"): -1,
    ("L", "I"): 2,
    ("X", "I"): -1,
    ("Z", "B"): 1,
    ("X", "E"): -1,
    ("Z", "N"): 0,
    ("X", "A"): 0,
    ("B", "R"): -1,
    ("B", "N"): 3,
    ("F", "D"): -3,
    ("X", "Y"): -1,
    ("Z", "R"): 0,
    ("F", "H"): -1,
    ("B", "F"): -3,
    ("F", "L"): 0,
    ("X", "Q"): -1,
    ("B", "B"): 4,
}


def score(s1, s2):
    if (s1, s2) in BLOSUM62:
        return BLOSUM62[(s1, s2)]
    else:
        return BLOSUM62[(s2, s1)]


def traceback(positions):
    maximum = max(positions)

    # diagonal
    if positions.index(maximum) == 0:
        return "\\"
    # esquerda
    elif positions.index(maximum) == 1:
        return "_"
    # cima
    elif positions.index(maximum) == 2:
        return "|"


def printMatrix(firstSequence, secondSequence, scoreMatrix, tracebackMatrix):
    print("\t", end="")
    for j in range(0, len(firstSequence)):
        print(firstSequence[j], end="\t")
    print()
    for i in range(0, len(secondSequence)):
        print(secondSequence[i], end="\t")
        for j in range(0, len(firstSequence)):
            print(scoreMatrix[i][j], tracebackMatrix[i][j], end="\t", sep="")
        print()
    print()


def alignment(firstSequence, secondSequence, scoreMatrix, tracebackMatrix):
    ali_first = ""
    ali_second = ""
    i = len(secondSequence) - 1
    j = len(firstSequence) - 1
    while (i != 0) or (j != 0):
        if tracebackMatrix[i][j] == "\\":
            ali_first = firstSequence[j] + ali_first
            ali_second = secondSequence[i] + ali_second
            i -= 1
            j -= 1
        elif tracebackMatrix[i][j] == "_":
            ali_first = firstSequence[j] + ali_first
            ali_second = "_" + ali_second
            j -= 1
        elif tracebackMatrix[i][j] == "|":
            ali_first = "_" + ali_first
            ali_second = secondSequence[i] + ali_second
            i -= 1
    print(
        "Pontuação do melhor alinhamento: ",
        scoreMatrix[len(secondSequence) - 1][len(firstSequence) - 1],
    )
    print("\n Sequência 1:")
    print(ali_first)
    print("\n Sequência 2:")
    print(ali_second)


def needlemanWunsch(firstSequence, secondSequence):
    scoreMatrix = []
    tracebackMatrix = []
    scoreMatrix = [0] * len(firstSequence)
    tracebackMatrix = [""] * len(firstSequence)

    # inicializa matriz de pontos e ponteiros com zeros e espaços
    for i in range(0, len(secondSequence)):
        scoreMatrix[i] = [0] * len(firstSequence)
        tracebackMatrix[i] = [""] * len(firstSequence)

    # inicializa a primeira coluna da matriz com barras
    for i in range(0, len(secondSequence)):
        tracebackMatrix[i][0] = "|"

    # inicializa a primeira linha da matriz com underscore
    for j in range(0, len(firstSequence)):
        tracebackMatrix[0][j] = "_"

    for i in range(1, len(secondSequence)):  # i = linha
        for j in range(1, len(firstSequence)):  # j = coluna
            s1 = firstSequence[j]
            s2 = secondSequence[i]

            cima = scoreMatrix[i - 1][j]
            esquerdo = scoreMatrix[i][j - 1]
            diagonal = scoreMatrix[i - 1][j - 1] + score(s1, s2)

            positions = [diagonal, esquerdo, cima]

            scoreMatrix[i][j] = max(positions)
            tracebackMatrix[i][j] = traceback(positions)

    printMatrix(firstSequence, secondSequence, scoreMatrix, tracebackMatrix)
    alignment(firstSequence, secondSequence, scoreMatrix, tracebackMatrix)
    input("Digite enter para voltar ao menu")


def validateSequence(sequence):
    for i in sequence:
        if i not in AMINOACID_CODES:
            return False

    return True


def inputSequence(sequenceNumber):
    isInvalidSequence = False

    while isInvalidSequence == False:
        sequence = input(f"Digite a {sequenceNumber} sequência: ").upper()
        isInvalidSequence = validateSequence(sequence)

        if isInvalidSequence == False:
            print("\nSequência inválida. Por favor, Informe uma sequência válida")
        else:
            return sequence


def customAlignment():
    print("\n######################################################################")
    print("\n#                  ALINHAMENTO DE SEQUÊNCIAS                         #")
    print("\n#                  Informe as sequências abaixo                      #")
    print("\n######################################################################")

    firstSequence = inputSequence("primeira")
    secondSequence = inputSequence("segunda")

    firstSequence = ["*"] + list(firstSequence)
    secondSequence = ["*"] + list(secondSequence)

    needlemanWunsch(firstSequence, secondSequence)


def exercise1():
    print("\n###########################################################################")
    print("\n#                          EXERCÍCIO 1                                    #")
    print("\n# Tente alinhar sequências idênticas e bem pequenas como DRQT por exemplo #")
    print("\n#-------------------------------------------------------------------------#")
    print("\n#                          RESPOSTA EXERCÍCIO 1:                          #")
    print("\n#-------------------------------------------------------------------------#")

    firstSequence = ["*", "D", "R", "Q", "T"]
    secondSequence = ["*", "D", "R", "Q", "T"]

    needlemanWunsch(firstSequence, secondSequence)

    print("\n#-----------------------------FIM EXERCÍCIO 1-----------------------------#")

def exercise2():
    print("\n##############################################################################################")
    print("\n#                          EXERCÍCIO 2                                                       #")
    print("\n# Faça pequenas alterações na sequência substituindo uma glutamina (Q) por um glutamato (E). #")
    print("\n#--------------------------------------------------------------------------------------------#")
    print("\n#                          RESPOSTA EXERCÍCIO 2:                                             #")
    print("\n#--------------------------------------------------------------------------------------------#")

    firstSequence = ["*", "D", "R", "Q", "T"]
    secondSequence = ["*", "D", "R", "E", "T"]

    needlemanWunsch(firstSequence, secondSequence)

    print("\n#-----------------------------FIM EXERCÍCIO 2-----------------------------#")


def exercise3():
    print("\n#######################################################################################################")
    print("\n#                          EXERCÍCIO 3                                                                #")
    print("\n# Alinhe sequências um pouco maiores e de comprimentos diferentes como DRQTAQAAGTTTIT e DRNTAQLLGTDTT #")
    print("\n#-----------------------------------------------------------------------------------------------------#")
    print("\n#                          RESPOSTA EXERCÍCIO 3:                                                      #")
    print("\n#-----------------------------------------------------------------------------------------------------#")

    firstSequence = ["*", "D","R","Q","T","A","Q","A","A","G","T","T","T","I","T"]
    secondSequence = ["*", "D","R","N","T","A","Q","L","L","G","T","D","T","T"]

    needlemanWunsch(firstSequence, secondSequence)

    print("\n#-----------------------------FIM EXERCÍCIO 3---------------------------------------------------------#")

def exercise4():
    print("\n#######################################################################################################")
    print("\n#                          EXERCÍCIO 4                                                                #")
    print("\n# Alinhe pares de sequências do SARS-CoV-2 e de outros vírus.                                         #")
    print("\n#-----------------------------------------------------------------------------------------------------#")
    print("\n#                          RESPOSTA EXERCÍCIO 4:                                                      #")
    print("\n#-----------------------------------------------------------------------------------------------------#")

    coronavirus1 = open("sequence_sarscov1.txt", "r")
    coronavirus2 = open("sequence_sarscov2.txt", "r")

    coronavirus1 = coronavirus1.read()
    coronavirus2 = coronavirus2.read()

    firstSequence = ["*"] + list(coronavirus2)
    secondSequence = ["*"] + list(coronavirus1)

    needlemanWunsch(firstSequence, secondSequence)

    print("\n#-----------------------------FIM EXERCÍCIO 4---------------------------------------------------------#")

def submenu ():
    while True:
        print("\n######################################################################")
        print("\n#                                                                    #")
        print("\n#                  Exercícios de Alinhamento                         #")
        print("\n#                        SUBMENU                                     #")
        print("\n# Opção 1 : Exercício 1                                              #")
        print("\n# Opção 2 : Exercício 2                                              #")
        print("\n# Opção 3 : Exercício 3                                              #")
        print("\n# Opção 4 : Exercício 4                                              #")
        print("\n# Opção 5 : Sair                                                     #")
        print("\n######################################################################")

        option = int(input("Digite a opção desejada: "))

        if option == 1:
            exercise1()
        elif option == 2:
            exercise2()
        elif option == 3:
            exercise3()
        elif option == 4:
            exercise4()
        else:
            return False               


def menu():
    while True:
        print("\n######################################################################")
        print("\n#                                                                    #")
        print("\n#Implementação do Algoritmo de Needleman-Wunsch com Matrix BLOSUM62  #")
        print("\n#                           MENU                                     #")
        print("\n# Opção 1 : Resolver exercícios                                      #")
        print("\n# Opção 2 : Alinhar própria sequência                                #")
        print("\n# Opção 3 : Sair                                                     #")
        print("\n######################################################################")

        option = int(input("Digite a opção desejada: "))

        if option == 1:
            submenu()
        elif option == 2:
            customAlignment()
        else: 
            return False           


menu()

