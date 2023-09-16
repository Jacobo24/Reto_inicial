def es_seguro(tablero, fila, columna, n):
    # Verificar si es seguro colocar una reina en la casilla (fila, columna)
    
    # Verificar la misma columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False
    
    # Verificar la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    # Verificar la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(columna, n)):
        if tablero[i][j] == 1:
            return False
    
    return True

def contar_soluciones_damas(n):
    def backtrack(fila):
        nonlocal soluciones
        if fila == n:
            soluciones += 1
            return
        for columna in range(n):
            if es_seguro(tablero, fila, columna, n):
                tablero[fila][columna] = 1
                backtrack(fila + 1)
                tablero[fila][columna] = 0
    
    tablero = [[0] * n for _ in range(n)]
    soluciones = 0
    backtrack(0)
    return soluciones

# Número de damas
N = 15

soluciones = contar_soluciones_damas(N)
print(f'Para n={N}, hay {soluciones} soluciones.')