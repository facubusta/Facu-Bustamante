import csv

#Ejercicio 1: Crear una función lambda que incremente un 10% en el sueldo recibido
incremento_10 = lambda sueldo: sueldo * 1.10
print(f"El sueldo con el incremento es de : {incremento_10(2000)}") 

#Ejercicio 2: Crear una función lambda que informe si una persona es mayor (mayor a
#17 años) o menor
es_mayor = lambda edad: f"{edad} es mayor" if edad > 17 else f"{edad} es menor"
print(es_mayor(18))
print(es_mayor(14))

#Ejercicio 3: Crear una función lambda que indique si el número recibido es par o impar.
es_par = lambda numero: f"El {numero} es par" if numero % 2 == 0 else f"El {numero} es impar"
print(es_par(4))
print(es_par(3))

#Ejercicio 4: Crear una función lambda que indique si el número recibido es positivo o negativo.
es_positivo = lambda numero: f"El {numero} es positivo" if numero >= 0 else f"El {numero} es negativo"
print(es_positivo(5))
print(es_positivo(-45))

#Ejercicio 5: Crear una función lambda que realice un 10% de descuento en el importe recibido
decremento = lambda importe: importe * 0.90
print(f"El importe con el 10% de descuento es : {decremento(100)} ")

#Ejercicio 6: Crear una función lambda devuelva el doble del número recibido.
doble = lambda numero: f"El doble de {numero} es {numero * 2}"
print(doble(4))

#Ejercicio 7: Crear una función lambda que devuelva el texto “femenino” si recibe el
#valor “f” y sino “masculino”.
genero = lambda letra: "Femenino" if letra == "f" or letra == "F" else "Masculino"
print(genero("F"))  
print(genero("M"))  

#Ejercicio 1: Crear una función que lea el archivo recibido y lo muestre por pantalla.
def leer_archivo(ruta_archivo: str) ->str:
    '''
    Lee archivos y lo muestra por pantalla
    '''
    with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
    return contenido
print(leer_archivo("Facu-Bustamante/Funciones Lambda y Archivos/archivo.txt"))

#Ejercicio 2: Crear una función que guarde una matriz como “.csv”.
def guardar_matriz_como_csv(matriz: list, nombre_archivo: str):
    '''
    Guarda una matriz (lista de listas) en un archivo .csv
    '''
    with open(nombre_archivo, "w") as archivo:
        for fila in matriz:
            linea = ""

            for i in range(len(fila)):
                linea += str(fila[i])

                if i < (len(fila) - 1):
                    linea += ","
        
            archivo.write(linea + "\n")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 11]]

guardar_matriz_como_csv(matriz, "Facu-Bustamante/Funciones Lambda y Archivos/archivo.txt")
