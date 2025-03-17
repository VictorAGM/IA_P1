from random import randrange


def mostrar_tablero(tablero):
    print("+-------" * 3, "+", sep="")
    for fila in range(3):
        print("|       " * 3, "|", sep="")
        for columna in range(3):
            print("|   " + str(tablero[fila][columna]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def ingresar_movimiento(tablero):
    valido = False  # Suponemos que la entrada es inválida al inicio
    while not valido:
        movimiento = input("Ingresa tu movimiento: ") 
        valido = len(movimiento) == 1 and '1' <= movimiento <= '9'  # ¿Es un número válido?
        if not valido:
            print("Movimiento erróneo, ingrésalo nuevamente")  # Entrada inválida
            continue
        movimiento = int(movimiento) - 1  # Convertimos la entrada a un índice (0-8)
        fila = movimiento // 3  # Calculamos la fila
        columna = movimiento % 3  # Calculamos la columna
        casilla = tablero[fila][columna]  # Obtenemos el valor de la casilla
        valido = casilla not in ['O', 'X'] 
        if not valido:  # Si la casilla está ocupada, pedimos otra entrada
            print("¡Casilla ocupada, ingresa nuevamente!")
            continue
    tablero[fila][columna] = 'O'  # Colocamos 'O' en la casilla seleccionada


def lista_casillas_libres(tablero):
    libres = []  # Lista vacía al inicio
    for fila in range(3):  # Iteramos sobre las filas
        for columna in range(3):  # Iteramos sobre las columnas
            if tablero[fila][columna] not in ['O', 'X']:  # ¿Está la casilla libre?
                libres.append((fila, columna))  # Si es así, la agregamos a la lista
    return libres


def verificar_victoria(tablero, simbolo):
    if simbolo == "X":  # ¿Estamos buscando X?
        ganador = 'computadora'  # Sí, es la máquina
    elif simbolo == "O":  # ¿O estamos buscando O?
        ganador = 'jugador'  # Sí, es el usuario
    else:
        ganador = None  # ¡No deberíamos llegar aquí!
    
    diagonal1 = diagonal2 = True  # Para verificar diagonales
    for rc in range(3):
        if tablero[rc][0] == simbolo and tablero[rc][1] == simbolo and tablero[rc][2] == simbolo:  # Verificar filas
            return ganador
        if tablero[0][rc] == simbolo and tablero[1][rc] == simbolo and tablero[2][rc] == simbolo:  # Verificar columnas
            return ganador
        if tablero[rc][rc] != simbolo:  # Revisar la primera diagonal
            diagonal1 = False
        if tablero[2 - rc][rc] != simbolo:  # Revisar la segunda diagonal
            diagonal2 = False
    if diagonal1 or diagonal2:
        return ganador
    return None


def movimiento_computadora(tablero):
    libres = lista_casillas_libres(tablero)  # Obtener lista de casillas vacías
    cantidad = len(libres)
    if cantidad > 0:  # Si hay casillas libres, colocar 'X' en una al azar
        eleccion = randrange(cantidad)
        fila, columna = libres[eleccion]
        tablero[fila][columna] = 'X'


# Crear el tablero inicial
tablero = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  
tablero[1][1] = 'X'  # La computadora coloca la primera 'X' en el centro
libres = lista_casillas_libres(tablero)
turno_humano = True  # ¿De quién es el turno?

while len(libres):
    mostrar_tablero(tablero)
    if turno_humano:
        ingresar_movimiento(tablero)
        ganador = verificar_victoria(tablero, 'O')
    else:
        movimiento_computadora(tablero)
        ganador = verificar_victoria(tablero, 'X')
    if ganador is not None:
        break
    turno_humano = not turno_humano  # Cambiar turno
    libres = lista_casillas_libres(tablero)

mostrar_tablero(tablero)
if ganador == 'jugador':
    print("¡Has ganado!")
elif ganador == 'computadora':
    print("¡He ganado!")
else:
    print("¡Empate!")
