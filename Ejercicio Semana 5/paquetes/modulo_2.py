#2- Crear una función que imprima por pantalla el tamaño de una matriz

def calcular_tamaño_matriz(matriz : list):
    '''Calcula el tamaño de una matriz'''

    for i in range(len(matriz)):
        filas = len(matriz)
        for j in range(len(matriz)):
            columnas = len(matriz[j])
    return f"El tamaño de la matriz es de {filas} x {columnas}"       


