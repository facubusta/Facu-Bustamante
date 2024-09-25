#11- Programar el algoritmo de búsqueda binaria de forma recursiva
def buscar_binariamente(lista, objetivo, bajo=0, alto=None):

    if alto is None:
        alto = len(lista) - 1

    if bajo > alto:
        return -1  

    medio = (bajo + alto) // 2

    if lista[medio] == objetivo:
        return medio  
    elif lista[medio] > objetivo:
        return buscar_binariamente(lista, objetivo, bajo, medio - 1) 
    else:
        return buscar_binariamente(lista, objetivo, medio + 1, alto)  

lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
objetivo = 7
resultado = buscar_binariamente(lista_ordenada, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en el índice: {resultado}")
else:
    print("Elemento no encontrado.")

