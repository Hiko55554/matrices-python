# ************   MÓDULOS ESPECÍFICOS DE LA APLICACIÓN  ***************

import copy

# -----------  Menu  -------------
def Menu():
    print()
    print('*****   OPERACIONES CON MATRICES   *****')
    print('1 Sumar')
    print('2 Multiplicar')
    print('3 Transpuesta')
    print('4 Inversa')
    print('5 Escalonar')
    print('6 Determinante')
    print('7 Adjunta')
    print('8 Rango')
    print('9 Resolver Sistema de Ecuaciones')
    print('10 FIN')

# -----------  Generar Matriz  -------------
def GenerarMatriz(NroFilas, NroColumnas):
    return [[None] * NroColumnas for _ in range(NroFilas)]

# -----------  Leer elementos de la Matriz  -------------
def LeerElementosMatriz(NroFilas, NroColumnas):
    Matriz = GenerarMatriz(NroFilas, NroColumnas)
    for F in range(NroFilas):
        for C in range(NroColumnas):
            print(f'Ingrese el elemento ({F+1},{C+1}): ', end='')
            Matriz[F][C] = float(input())
    return Matriz

# -----------  Leer Matriz  -------------
def LeerMatriz():
    NroFilas = int(input("Ingrese el número de filas de la Matriz: "))
    NroColumnas = int(input("Ingrese el número de columnas de la Matriz: "))
    Matriz = LeerElementosMatriz(NroFilas, NroColumnas)
    return NroFilas, NroColumnas, Matriz

# -----------  Escribir Matriz  -------------
def EscribirMatriz(NroFilas, NroColumnas, Matriz):
    for F in range(NroFilas):
        for C in range(NroColumnas):
            print(round(Matriz[F][C], 2), '\t', end='')
        print()

# -----------  Sumar Matrices  -------------
def SumarMatrices(NroFilas, NroColumnas, Matriz1, Matriz2):
    MatrizS = GenerarMatriz(NroFilas, NroColumnas)
    for F in range(NroFilas):
        for C in range(NroColumnas):
            MatrizS[F][C] = Matriz1[F][C] + Matriz2[F][C]
    return NroFilas, NroColumnas, MatrizS

def SumaDeMatrices():
    print('\nINGRESE LOS DATOS DE LA PRIMERA MATRIZ')
    NroFilas, NroColumnas, Matriz1 = LeerMatriz()
    print('\nINGRESE LOS DATOS DE LA SEGUNDA MATRIZ')
    Matriz2 = LeerElementosMatriz(NroFilas, NroColumnas)
    NroFilasS, NroColumnasS, MatrizS = SumarMatrices(NroFilas, NroColumnas, Matriz1, Matriz2)
    print('\nRESULTADO DE LA SUMA:')
    EscribirMatriz(NroFilasS, NroColumnasS, MatrizS)

# -----------  Multiplicación de Matrices  -------------
def MultiplicarMatrices(F1, C1, M1, F2, C2, M2):
    MatrizR = GenerarMatriz(F1, C2)
    for i in range(F1):
        for j in range(C2):
            suma = 0
            for k in range(C1):
                suma += M1[i][k] * M2[k][j]
            MatrizR[i][j] = suma
    return F1, C2, MatrizR

def MultiplicacionDeMatrices():
    print('\nINGRESE LOS DATOS DE LA PRIMERA MATRIZ')
    F1, C1, M1 = LeerMatriz()
    print('\nINGRESE LOS DATOS DE LA SEGUNDA MATRIZ')
    F2, C2, M2 = LeerMatriz()
    if C1 != F2:
        print("¡No se pueden multiplicar! El número de columnas de la primera debe coincidir con el número de filas de la segunda.")
        return
    FR, CR, MR = MultiplicarMatrices(F1, C1, M1, F2, C2, M2)
    print('\nRESULTADO DE LA MULTIPLICACIÓN:')
    EscribirMatriz(FR, CR, MR)

# -----------  Transpuesta  -------------
def Transpuesta(F, C, M):
    MT = GenerarMatriz(C, F)
    for i in range(F):
        for j in range(C):
            MT[j][i] = M[i][j]
    return C, F, MT

def TranspuestaDeMatriz():
    print('\nINGRESE LOS DATOS DE LA MATRIZ')
    F, C, M = LeerMatriz()
    FT, CT, MT = Transpuesta(F, C, M)
    print('\nTRANSPUESTA DE LA MATRIZ:')
    EscribirMatriz(FT, CT, MT)

# -----------  Determinante  -------------
def Determinante(M):
    if len(M) == 1:
        return M[0][0]
    if len(M) == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    det = 0
    for c in range(len(M)):
        submat = [row[:c] + row[c+1:] for row in M[1:]]
        det += ((-1)**c) * M[0][c] * Determinante(submat)
    return det

def DeterminanteDeMatriz():
    F, C, M = LeerMatriz()
    if F != C:
        print("¡La matriz debe ser cuadrada!")
        return
    print(f"\nDETERMINANTE: {Determinante(M)}")

# -----------  Escalonamiento y Rango  -------------
def Escalonar(M):
    A = copy.deepcopy(M)
    filas = len(A)
    columnas = len(A[0])
    fila_actual = 0
    for col in range(columnas):
        if fila_actual >= filas:
            break
        i = fila_actual
        while i < filas and abs(A[i][col]) < 1e-10:
            i += 1
        if i == filas:
            continue
        A[fila_actual], A[i] = A[i], A[fila_actual]
        pivote = A[fila_actual][col]
        A[fila_actual] = [x / pivote for x in A[fila_actual]]
        for i in range(filas):
            if i != fila_actual:
                factor = A[i][col]
                A[i] = [A[i][j] - factor * A[fila_actual][j] for j in range(columnas)]
        fila_actual += 1
    return A

def EscalonarMatriz():
    F, C, M = LeerMatriz()
    ME = Escalonar(M)
    print('\nMATRIZ ESCALONADA:')
    EscribirMatriz(F, C, ME)

def RangoMatriz():
    F, C, M = LeerMatriz()
    escalonada = Escalonar(M)
    rango = sum(any(abs(val) > 1e-10 for val in fila) for fila in escalonada)
    print(f"\nRANGO DE LA MATRIZ: {rango}")

# -----------  Adjunta e Inversa  -------------
def Cofactor(M, i, j):
    return [[M[x][y] for y in range(len(M)) if y != j] for x in range(len(M)) if x != i]

def Adjunta(M):
    n = len(M)
    return [[(-1)**(i+j) * Determinante(Cofactor(M, i, j)) for j in range(n)] for i in range(n)]

def InversaDeMatriz():
    F, C, M = LeerMatriz()
    if F != C:
        print("¡La matriz debe ser cuadrada!")
        return
    det = Determinante(M)
    if abs(det) < 1e-10:
        print("¡La matriz no tiene inversa (determinante = 0)!")
        return
    adj = Adjunta(M)
    adj_T = Transpuesta(F, C, adj)[2]
    inversa = [[adj_T[i][j] / det for j in range(C)] for i in range(F)]
    print("\nINVERSA DE LA MATRIZ:")
    EscribirMatriz(F, C, inversa)

def AdjuntaDeMatriz():
    F, C, M = LeerMatriz()
    if F != C:
        print("¡La matriz debe ser cuadrada!")
        return
    adj = Adjunta(M)
    print("\nMATRIZ ADJUNTA:")
    EscribirMatriz(F, C, adj)

# -----------  Sistema de Ecuaciones Lineales -------------
def ResolverSistemaEcuaciones():
    print('\nINGRESE LA MATRIZ AUMENTADA DEL SISTEMA (coeficientes + término independiente)')
    F, C, M = LeerMatriz()
    if C != F + 1:
        print("¡La matriz aumentada debe tener una columna más que filas!")
        return
    ME = Escalonar(M)
    solucion = [0 for _ in range(F)]
    for i in range(F - 1, -1, -1):
        solucion[i] = ME[i][-1] - sum(ME[i][j] * solucion[j] for j in range(i + 1, F))
    print('\nSOLUCIÓN DEL SISTEMA:')
    for i, val in enumerate(solucion):
        print(f"x{i + 1} = {round(val, 4)}")

# *****************   PROGRAMA PRINCIPAL   *******************

print('======================================')
print(' Escanea el código QR con tu celular.')
print(' Cuando termines, presiona ENTER...')
print('======================================')
input()

Opcion = 0
while Opcion != 10:
    Menu()
    try:
        Opcion = int(input('Ingrese opción --> '))
        if Opcion == 1:
            SumaDeMatrices()
        elif Opcion == 2:
            MultiplicacionDeMatrices()
        elif Opcion == 3:
            TranspuestaDeMatriz()
        elif Opcion == 4:
            InversaDeMatriz()
        elif Opcion == 5:
            EscalonarMatriz()
        elif Opcion == 6:
            DeterminanteDeMatriz()
        elif Opcion == 7:
            AdjuntaDeMatriz()
        elif Opcion == 8:
            RangoMatriz()
        elif Opcion == 9:
            ResolverSistemaEcuaciones()
        elif Opcion == 10:
            print('Programa finalizado.')
        else:
            print('¡Opción inválida!')
    except ValueError:
        print("Por favor, ingrese un número válido.")
