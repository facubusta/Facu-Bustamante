#Ejercicio 3:
#Desarrollar una función que realice el ordenamiento de las listas por apellido de
#manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
#ascendente, si el nombre también es el mismo, debe ordenar por nota de maner adescendente.



def ordenar_por_apellido(estudiantes : list, apellidos : list, nota : list) ->list:
    '''
    Ordena por apellido de manera ascendente.
    Si es el mismo apellido, ordena por nombre de manera ascendente.
    Si es el mismo nombre, ordena por nota de manera ascendente.
    '''

    if type(estudiantes) != list and type(apellidos) != list and type(nota) != list:
        return print("Los nombres y edades deben ser unas listas")
    


