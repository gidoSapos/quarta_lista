def sum_principal_diagonal() -> int:
    matriz_completa, soma_diagonal = [], 0
    while True:
        try:
            for i in range (3):
                linha = [int(num.strip()) for num in input(f'Insira o valor {i + 1} desejado dawg: ').split(',')]
                if len(linha) != 3: raise ValueError('Deve conter 3 elementos.')
                matriz_completa.append(linha)

            soma_diagonal = matriz_completa[0][0] + matriz_completa[1][1] + matriz_completa[2][2]
            print(soma_diagonal)
            break

        except ValueError as ERROR:
            print(f'Erro {ERROR} Por favor insira apenas valores númericos.') 


def sum_secundaria_diagonal():
    matriz_completa, soma_diagonal = [], 0
    while True:
        try:
    
            for i in range (3):
                lista = [int(num.strip()) for num in input(f'Insira o valor {i + 1} desejado zeca urubu: ').split(',')]
                if len(lista) != 3: raise ValueError('matriz 3 por 3 apenas')
                matriz_completa.append(lista)
            soma_diagonal = matriz_completa[0][2] + matriz_completa[1][1] + matriz_completa[2][0]
            return soma_diagonal
        
        except ValueError as ERROR:
            print(f'Erro {ERROR} Por favor insira apenas valores númericos.') 


def sumOfTwoMatriz():
    matriz_completa1 = matriz_completa2 = []
    while True:
        try:
            print('Para a primeira matriz: ')
            for i in range (3):
                lista1 = [int(num.strip()) for num in input(f'Insira o valor {i + 1} desejado dawg: ').split(',')]
                if len(lista1 ) != 3: raise ValueError('Deve conter 3 elementos.')
                matriz_completa1.append(lista1 )

            print('Para a segunda matriz: ')
            for i in range (3):
                lista2 = [int(num.strip()) for num in input(f'Insira o valor {i + 1} desejado dawg: ').split(',')]
                if len(lista2) != 3: raise ValueError('Deve conter 3 elementos.')
                matriz_completa1.append(lista2)

            soma_matrizes = [[matriz_completa1[i][j] + matriz_completa2[i][j] for j in range (3)] for i in range (3)]
            return soma_matrizes
        except ValueError as ERROR:
            print(f'Erro {ERROR} Por favor insira apenas valores númericos.')   


def maxMinMatriz() -> tuple:
    matriz_completa = []
    while True:
        try:
            for i in range (3):
                lista= [int(num.strip()) for num in input(f'Insira o valor {i + 1} desejado dawg: ').split(',')]
                if len(lista) != 3: raise ValueError('matriz 3 por 3 apenas')
                matriz_completa.append(lista) 

            return max(max(numero) for numero in matriz_completa), min(min(numero) for numero in matriz_completa)
        except ValueError as ERROR: print(f'Erro {ERROR} Por favor insira apenas valores númericos.')   


def avarageMatriz() -> float:
    matriz_completa = [ ]
    while True:
        try:
            for i in range(3): 
                linha = [float(num.strip())for num in input(f'Insira {i + 1} valores que deseja: ').split(',')]
                if len(linha) != 3: raise ValueError('matriz 3 por 3 apenas.')
                matriz_completa.append(linha)
        
            return sum(sum(numberos) for numberos in matriz_completa) / 9
        except ValueError as e: print(f'DEU MERDA! {e} vc eh burrao')


def negativeToZero():
    matriz_completa = []
    while True:
        try:
            for i in range(3):
                lista = [float(num.strip()) for num in input(f'Insira o {i + 1} nomberos: ').split(',')]
                if len(lista) != 3: raise ValueError('WORF WORF WORFFF!!')
                matriz_completa.append(lista)

            lista_semZero = []
            for lista in matriz_completa:
                novos_nomberos = []
                for num in lista:
                    if num < 0:
                        novos_nomberos.append(0)
                    else:
                        novos_nomberos.append(num)
                lista_semZero.append(novos_nomberos)

            return lista_semZero
        except ValueError as erro: print(f'EORRO {erro}: os macacos comeram suas bananas')


def productMatriz():
    matriz_completa1 = matriz_completa2 = []
    while True:
        try:

            for i in range(3):
                lista_recebedora = [int(num.strip()) for num in input(f'INSIRA {i + 1} NOMBEROS (MATRIZ 1): ').split(',')]
                if len(lista_recebedora) != 3: raise ValueError('Apenas 3x3')
                matriz_completa1.append(lista_recebedora)

            for i in range(3):
                matriz = [int(num.strip()) for num in input(f'INSIRA {i + 1} MOMEROS (MATRIZ 2): ').split(',')]
                if len(matriz) != 3: raise ValueError('Apenas 3x3')
                matriz_completa2.append(matriz)

            produto_matriz = [[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]

            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        produto_matriz[i][j] += matriz_completa1[i][k] * matriz_completa2[k][j]

            print("Produto das matrizes:")
            for linha in produto_matriz:
                print(" ".join(str(num) for num in linha))
            break

        except ValueError as e: print(f'{e}: não é permitido strings')


def imprime_matriz_transposta():
    matriz = []
    for i in range(3):
        linha = input(f"Insira a linha {i + 1} (separado por virgula): ").split(',')
        linha = [int(num.strip()) for num in linha]
        matriz.append(linha)

    if len(matriz) != 3 or any(len(linha) != 3 for linha in matriz):
        print("Erro: A matriz não é 3x3")
        return

    matriz_transposta = [[0, 0, 0],
                        [0, 0, 0], 
                        [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            matriz_transposta[j][i] = matriz[i][j]

    print("Matriz transposta:")
    for linha in matriz_transposta:
        print(" ".join(str(num) for num in linha))

def matriz_simetrica():
    while True:
        try:
            
            matriz = []
            for i in range(3):
                linha = input(f"Insira a linha {i+1} (separado por virgula): ").split(',')
                linha = [int(num.strip()) for num in linha]
                if len(linha) != 3:
                    raise ValueError("A matriz deve ter 3 colunas")
                matriz.append(linha)

            is_simetrica = True
            for i in range(3):
                for j in range(3):
                    if matriz[i][j] != matriz[j][i]:
                        is_simetrica = False
                        break

            if is_simetrica:
                print("A matriz é simétrica")
            else:
                print("A matriz não é simétrica")

            print("Matriz:")
            for linha in matriz:
                print(" ".join(str(num) for num in linha))

        except ValueError as e:
            print(f"Erro: {e}")

def calcula_determinante(matriz):
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[0][2]
    d = matriz[1][0]
    e = matriz[1][1]
    f = matriz[1][2]
    g = matriz[2][0]
    h = matriz[2][1]
    i = matriz[2][2]

    determinante = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return determinante

def matriz_determinante():
    while True:
        try:
            matriz = []
            for i in range(3):
                linha = input(f"Insira a linha {i + 1} (separado por virgula): ").split(',')
                linha = [int(num.strip()) for num in linha]
                if len(linha) != 3:
                    raise ValueError("A matriz deve ter 3 colunas")
                matriz.append(linha)

            determinante = calcula_determinante(matriz)
            print("Determinante da matriz:")
            print(determinante)

            print("Matriz:")
            for linha in matriz:
                print(" ".join(str(num) for num in linha))
            break
        except ValueError as e: print(f"Erro: {e}")
          