#6- Dada la siguiente lista de ingresos horarios:
#[ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
#9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
#a) Calcular el promedio de ingresos/hora del 20% que menos gana. No es necesario
#ordenar, utilizar listas anidadas y resolver usando listas.

ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]

n = len(ingresos)
porcentaje_20 = n // 5 

menos_ganadores = [0] * porcentaje_20 
contador = 0  

while contador < porcentaje_20:
    menor = float('inf') 
    for ingreso in ingresos:
        encontrado = False
        for chico in menos_ganadores:
            if ingreso == chico:
                encontrado = True
                break
        if ingreso < menor and encontrado == False:
            menor = ingreso
    menos_ganadores[contador] = menor  
    contador += 1  

suma = 0
for ingreso in menos_ganadores:
    suma += ingreso

promedio = suma / porcentaje_20

print(f"El promedio de ingresos/hora del 20% que menos gana es de: {promedio}")

        
