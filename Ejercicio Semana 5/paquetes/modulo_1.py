#1- Crear una función que agregue una columna a una matriz existente. No se pueden usar
#funciones preexistentes como append, se debe resolver con lo visto en las clases.
#(concatenar)

def agregar_columna(matriz: list, nueva_columna: any) -> list:  
    '''Agrega una columna a una matriz existente'''  

    if type(matriz) != list:    
        print("La función debe recibir una lista")
        return None
    if len(matriz) != len(nueva_columna):
        print("Debe recibir por parametro la misma cantidad de filas")
        return None
    
    nueva_matriz = [0] * len(matriz)
    
    for i in range(len(matriz)):
        nueva_matriz[i] = matriz[i] + [nueva_columna[i]]
    return nueva_matriz


    


    