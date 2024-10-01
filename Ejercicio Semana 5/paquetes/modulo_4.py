#7 - Crear una función que multiplique matrices. Verificar previamente que las matrices
#puedan ser multiplicadas

def multiplicar_matrices(matriz_a, matriz_b):
    '''Multiplica las matrices si se puede'''

    filas_a = len(matriz_a)         
    columnas_a = len(matriz_a[0])   
    filas_b = len(matriz_b)          
    columnas_b = len(matriz_b[0])   
    
    if columnas_a != filas_b:
        return "Las matrices no se pueden multiplicar."
    
    resultado =  [[0] * len(matriz_a), [0] * len(matriz_b[0])]

    for i in range(filas_a):  
        for j in range(columnas_b): 
            for k in range(columnas_a):  
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    
    return resultado

