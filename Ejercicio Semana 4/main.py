from paquetes.Modulo_4 import *
from paquetes.Modulo_5 import *
from paquetes.Modulo_6 import *
from paquetes.Modulo_7 import *
from paquetes.Modulo_8 import *
from paquetes.Modulo_9 import *


lista = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
        9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]

print(calcular_media_por_cuartil([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]))

print(corregir_lista(lista, 9, 100 ))

rango_inferior = float(input("Ingrese el límite inferior del rango: "))
rango_superior = float(input("Ingrese el límite superior del rango: "))
numeros_guardados = solicitar_numeros(rango_inferior, rango_superior)
print("Los números ingresados son:", numeros_guardados)

buscar_menores(nombres, edades)

print(verificar_tipos_lista([1, 'dos', 3.0]))      

mi_lista = [1, 2, 3]
print(cargar_valor(mi_lista, 4)) 













