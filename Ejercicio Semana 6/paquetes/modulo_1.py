#Ejercicio 1:
#Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente.

def ordenar_nombres(nombres : list, edades : list) -> list:
    '''Ordena los nombres de manera ascendente'''
    
    if type(nombres) != list and type(edades) != list:
        return print("Los nombres y edades deben ser unas listas")
    
    for i in range(len(nombres)):
        for j in range (0, len(nombres) - i - 1):
            if nombres[j] > nombres[j + 1]:
                nombre_mayor = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = nombre_mayor

                mayor_edad = edades[j]
                edades[j] = edades [j + 1]
                edades[j + 1] = mayor_edad

    return nombres, edades