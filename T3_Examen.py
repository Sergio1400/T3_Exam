# Este es nuestro laberinto de 9x9 como en la imagen
# (El Final está en [0][0] y el Inicio en [8][0])
laberinto = [
    [1, 0, 0, 3, 0, 0, 0, 0, 0],  # fila 0
    [0, 1, 1, 0, 0, 4, 1, 0, 0],  # fila 1
    [3, 0, 1, 3, 0, 1, 0, 4, 0],  # fila 2
    [0, 0, 0, 1, 1, 0, 0, 0, 0],  # fila 3
    [0, 3, 0, 0, 0, 0, 4, 0, 0],  # fila 4
    [0, 0, 1, 1, 0, 0, 0, 3, 0],  # fila 5
    [1, 0, 0, 0, 0, 3, 0, 0, 0],  # fila 6
    [1, 0, 3, 0, 1, 0, 4, 1, 0],  # fila 7
    [1, 1, 0, 0, 0, 0, 0, 0, 0],  # fila 8
]

# Usaremos esta matriz vacía para marcar el camino recorrido:
camino = [[0 for _ in range(9)] for _ in range(9)]

# Ahora vamos a hacer una funcion que nos diga a que posicion
# se a mover el raton del ejercicio:
def es_valido(x, y):
    return 0 <= x < 9 and 0 <= y < 9 and laberinto[x][y] != 0

# Ahora viene lo complicado, pues programamos las direcciones y caminos que tomara el raton:

# Si se llego a la salida:
def encontrar_camino(x, y, puntos):
    # Si llegó:
    if x == 0 and y == 0:
        if puntos >= 23:
            camino[x][y] = 1
            return True
        # Sino:
        else:
            return False
        
# Si se puede estar en la posicion actual:
    if not es_valido(x, y) or camino[x][y] == 1:
        return False
    
# Poder marca la casilla como parte del camino:
    camino[x][y] = 1

# Sumar puntos si es 3 o 4
    if laberinto[x][y] == 3 or laberinto[x][y] == 4:
        puntos += laberinto[x][y]

# Funcion para los movimientos: arriba, derecha, abajo, izquierda
    movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for dx, dy in movimientos:
        nuevo_x = x + dx
        nuevo_y = y + dy
        if encontrar_camino(nuevo_x, nuevo_y, puntos):
            return True

# Si no funcionó, desmarcamos la casilla con esta funcion (Aqui se usara backtracking):
    camino[x][y] = 0
    return False

# Ahora pondremos la ubicacion del inicio (Este seria en {8}{0}):
inicio_x, inicio_y = 8, 0
salida = encontrar_camino(inicio_x, inicio_y, 0) #El 0 del final son nuestros puntos
# para terminar, pongamos los finales de haber podido salir o no:
if salida:
    print("Se logro encontrar el camino con 23 o más puntos, felicidades")
else:
    print("No se encontró un camino por faltas de puntos :c")

# por ultimo mostrar el camino marcado
for fila in camino:
    print(fila)