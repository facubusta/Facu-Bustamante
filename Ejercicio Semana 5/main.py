from paquetes.modulo_1 import *
from paquetes.modulo_2 import *
from paquetes.modulo_3 import *
from paquetes.modulo_4 import *
from paquetes.modulo_5 import *

#Ejercicio_1
matriz_original = [[1, 2], [3, 4], [5, 6]]
nueva_columna = [7, 8, 9]
print(f"La nueva matriz sera: {agregar_columna(matriz_original, nueva_columna)}")

#Ejercicio_2
print(calcular_tamaño_matriz(matriz_original)) 

#Ejercicio_5
print(calcular_media([[1, 2, 3], [1, 2, 10]]))

#Ejercicio_7
matriz_a = [[1, 2, 3], 
            [4, 5, 20]]

matriz_b = [[7, 40], 
            [9, 10], 
            [11, 12]]

print(multiplicar_matrices(matriz_a, matriz_b))

#Ejercicio_8
print(f"La matriz tranpuesta de {matriz_a} es:")
print(calcular_matriz_transpuesta(matriz_a))













