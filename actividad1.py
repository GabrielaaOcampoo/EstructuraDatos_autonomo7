# Gabriela Ocampo - Implementación de búsqueda secuencial y binaria

# 🌟 Búsqueda secuencial
def busqueda_secuencial(lista, objetivo):
    """
    Como quien recorre un camino sin señales,
    vamos elemento por elemento, sin prisas pero sin pausa,
    esperando que, en algún rincón, aparezca lo que buscamos.
    Devuelve el índice del hallazgo y las veces que el corazón se ilusionó.
    """
    comparaciones = 0
    for i, elemento in enumerate(lista):
        comparaciones += 1
        if elemento == objetivo:
            return i, comparaciones
    return -1, comparaciones  # A veces el destino no está donde uno esperaba

# Búsqueda binaria
def busqueda_binaria(lista, objetivo):
    """
    Aquí la lógica es brújula y la lista es mapa.
    No caminamos todos los tramos, solo los justos.
    Cada paso reduce el mundo a la mitad, como quien decide con firmeza.
    Devuelve el índice del encuentro y las decisiones tomadas en el proceso.
    """
    bajo = 0
    alto = len(lista) - 1
    comparaciones = 0
    while bajo <= alto:
        comparaciones += 1
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio, comparaciones
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1, comparaciones  # Porque también en la lógica cabe la incertidumbre

# Lista ordenada — porque a veces el orden es la mitad del camino
A = [3, 7, 12, 18, 23, 31, 45, 52, 66, 78]
elemento_a_buscar = 31

# Prueba búsqueda secuencial — cuando el corazón busca sin algoritmo
indice_s, pasos_s = busqueda_secuencial(A, elemento_a_buscar)
print(f"Búsqueda Secuencial -> Índice encontrado: {indice_s}, Comparaciones: {pasos_s}")

# Prueba búsqueda binaria — cuando la lógica se convierte en arte
indice_b, pasos_b = busqueda_binaria(A, elemento_a_buscar)
print(f"Búsqueda Binaria -> Índice encontrado: {indice_b}, Comparaciones: {pasos_b}")

# 🌟 Si puedes soñarlo, puedes programarlo :) — porque cada línea también escribe una historia
