tablero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [None, 0, None]
]

n = 2  # Número de movimientos

def contar_movimientos_tablero(tablero, n):
    movimientos = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]

    def contar_movimientos_desde(fila, columna, movimientos_restantes):
        if movimientos_restantes == 0:
            return 1

        movimientos_validos = 0
        for mov in movimientos:
            nueva_fila = fila + mov[0]
            nueva_columna = columna + mov[1]
            if 0 <= nueva_fila < len(tablero) and 0 <= nueva_columna < len(tablero[0]) and tablero[nueva_fila][nueva_columna] is not None:
                movimientos_validos += contar_movimientos_desde(nueva_fila, nueva_columna, movimientos_restantes - 1)

        return movimientos_validos

    total_movimientos = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            if tablero[fila][columna] is not None:
                total_movimientos += contar_movimientos_desde(fila, columna, n - 1)

    return total_movimientos

total = contar_movimientos_tablero(tablero, n+1)
print(f"Total de movimientos posibles en {n} movimientos: {total}")