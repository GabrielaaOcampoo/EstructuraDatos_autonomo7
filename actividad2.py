# Gabriela Ocampo - Implementación de búsquedas en diferentes estructuras

# a) Búsqueda secuencial en lista desordenada
def busqueda_secuencial(lista, objetivo):
    """
    Como quien revisa una caja de recuerdos, vamos uno por uno,
    hasta que aparece justo eso que buscábamos sin saber dónde estaba.
    Retorna el índice del hallazgo y los pasos dados en el camino.
    """
    pasos = 0
    for i, valor in enumerate(lista):
        pasos += 1
        if valor == objetivo:
            return i, pasos
    return -1, pasos  # A veces el recuerdo no está donde lo esperábamos

# b) Búsqueda binaria en lista ordenada
def busqueda_binaria(lista, objetivo):
    """
    Aquí no se trata de mirar todo, sino de elegir con astucia,
    de dividir la duda y acercarse al centro con cada intento.
    Solo los datos ordenados permiten este tipo de intuición matemática.
    Retorna el índice del acierto y la cantidad de pasos razonados.
    """
    bajo = 0
    alto = len(lista) - 1
    pasos = 0
    while bajo <= alto:
        pasos += 1
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio, pasos
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1, pasos  # Y si no se halla, también es una respuesta

# c) Búsqueda en matriz 2D (fila por fila y columna por columna)
def busqueda_matriz(matriz, objetivo):
    """
    Como recorrer una ciudad por sus calles y avenidas,
    esta búsqueda se hace paso a paso, fila a fila,
    columna a columna, hasta dar con el destino buscado.
    Retorna la coordenada del hallazgo y los pasos del trayecto.
    """
    pasos = 0
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            pasos += 1
            if valor == objetivo:
                return (i, j), pasos
    return (-1, -1), pasos  # Porque incluso perderse es parte del mapa

# Datos de prueba — porque ningún poema se escribe sin tinta
lista_desordenada = [42, 13, 5, 77, 24]
lista_ordenada = [5, 13, 24, 42, 77]
matriz = [
    [1, 4, 6],
    [10, 14, 18],
    [20, 25, 30]
]

objetivo = 14

# Ejecución de cada método — que cada búsqueda tenga su momento

# Búsqueda secuencial: sin orden, pero con esperanza
indice_s, pasos_s = busqueda_secuencial(lista_desordenada, objetivo)
print(f"Búsqueda Secuencial en lista desordenada: Índice {indice_s}, Pasos {pasos_s}")

# Búsqueda binaria: lógica afilada en caminos rectos
indice_b, pasos_b = busqueda_binaria(lista_ordenada, objetivo)
print(f"Búsqueda Binaria en lista ordenada: Índice {indice_b}, Pasos {pasos_b}")

# Búsqueda en matriz: un paseo por el laberinto cuadriculado
posicion_m, pasos_m = busqueda_matriz(matriz, objetivo)
print(f"Búsqueda en matriz: Posición {posicion_m}, Pasos {pasos_m}")

# Si puedes soñarlo, puedes programarlo :) — Porque el código también es poesía jejeje
