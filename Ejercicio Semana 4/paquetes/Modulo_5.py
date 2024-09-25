#5- Realizar una función que permita corregir las listas del ejercicio 3 en caso de ser
#necesario. Para ello se debe poder acceder a una posición particular y cargar nuevos
#valores para el listado con valor incorrecto en dicha posición.

def corregir_lista(lista, posicion, nuevo_valor):
    """ Corrige un valor en la lista en la posición especificada."""
    if posicion < 0 or posicion >= len(lista):
        return "Error: La posición es inválida."
    lista[posicion] = nuevo_valor
    return lista

ingresos = [1000, 2000, 3000, 4000, 5000]
print("Lista original:", ingresos)

ingresos_corregidos = corregir_lista(ingresos, 0, 80000)

print("Lista corregida:", ingresos_corregidos)
     
   

