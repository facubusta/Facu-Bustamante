# Ejercicio 2:
#Desarrollar una función que realice el ordenamiento de las listas por nombre de
#manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
#descendente.

def ordenar_nombres_puntos(nombres : list, puntos : list) -> list:
    '''
    Ordena los nombres de manera ascendente y si se
    repite los nombres lo ordena de manera descendente
    '''
    
    if type(nombres) != list and type(puntos) != list:
        return print("Los nombres y edades deben ser unas listas")
    
    for i in range(len(nombres)):
        for j in range (0, len(nombres) - i - 1):
            if nombres[j] > nombres[j + 1]:
                nombre_mayor = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = nombre_mayor
                mayor_puntos = puntos[j]
                puntos[j] = puntos [j + 1]
                puntos[j + 1] = mayor_puntos

            if nombres[j] == nombres[j + 1] and puntos[j] < puntos [j + 1]:
                mayor_puntos = puntos[j]
                puntos[j] = puntos[j + 1]
                puntos[j + 1] = mayor_puntos


    return nombres, puntos

