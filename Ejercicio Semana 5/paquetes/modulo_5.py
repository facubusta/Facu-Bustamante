#8 -. Ver el apunte de algoritmos matemáticos y generar una función que devuelva una
#matriz transpuesta.

def calcular_matriz_transpuesta(matriz : list) -> list:
    '''Calcula la transpuesta de una matriz'''

 
    matriz_transpuesta = [0 * range(len(matriz)), 0 * len(matriz[0])]

    for i in range(len(matriz)):      
        for j in range(len(matriz[0])):  
            matriz_transpuesta[j][i] = matriz[i][j]  
            
    return matriz_transpuesta


