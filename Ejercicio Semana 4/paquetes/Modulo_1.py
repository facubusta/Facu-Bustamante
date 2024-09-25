#A
lista = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]

def calcular_top_20(lista: list):
    '''Calcula la suma del top 20 y luego saca el promedio'''

    mayores = [float('-inf')] * 4
   
    for ingreso in lista:
        for i in range(4):
            if ingreso > mayores[i]:
                for j in range(3, i, -1):
                    mayores[j] = mayores[j - 1]
                mayores[i] = ingreso  
                break

    total = 0
    for valor in mayores:
        total += valor  

    promedio = total / 4  
    return promedio
   
promedio_top_4= calcular_top_20(lista)
print(f"El promedio de los 4 ingresos más altos es de : {promedio_top_4}")

#B
def calcular_promedio_todos(lista: list) -> float:
    '''Calcula el promedio de todos'''

    total = 0
    for i in range(len(lista)):
        total += lista[i]
    
    promedio_total = total / len(lista)
    return promedio_total

promedio_general = calcular_promedio_todos(lista)

print(f"El promedio de ingresos/hora de todos los respondentes es de : {promedio_general}")

#C
def buscar_repetidos(lista: list) -> float:
    '''Busca los numeros reptidos dentro de una lista'''

    repetidos = [0] * len(lista)
    conteo = [0] * len(lista)
    cantidad_repetidos = 0

    for num in lista:
        bandera = False
        for i in range (cantidad_repetidos):
            if repetidos[i] == num:
                conteo[i] += 1
                bandera = True
                break

        if not bandera:
            repetidos[cantidad_repetidos] = num  
            conteo[cantidad_repetidos] = 1        
            cantidad_repetidos += 1         

    cant_repetidos = 0
    for i in range(cantidad_repetidos):
        if conteo[i] > cant_repetidos:
            cant_repetidos = conteo[i]

    numeros_repetidos = []
    for i in range(cantidad_repetidos):
        if conteo[i] == cant_repetidos:
            numeros_repetidos += [repetidos[i]] 

    return cant_repetidos, numeros_repetidos  

repetidos, numeros_repetidos = buscar_repetidos(lista)
print(f"Las veces que se repiten los numeros son : {repetidos} y ellos son : {numeros_repetidos}")

def calcular_media_geometrica(lista: list) -> float:
    '''Calcula la media geometrica'''

    producto = 1
    for num in lista:
        producto *= num
    
    raiz = len(lista)
    media_geometrica = producto **(1/raiz)
    return media_geometrica

total_geometria = calcular_media_geometrica(lista)
print(f"La media geométrica es: {total_geometria}")

def recorrer_listas(lista: list) -> float:
    '''Recorre la lista hacia adelante y hacia atras'''

    for num in lista:
        print(num)

    for i in range(len(lista) -1, -1, -1):
        print(lista[i])  

recorrer = recorrer_listas(lista)
print(f"Recorrido hacia adelante y luego hacia atras : {recorrer}")

    




    

    

    

    





            
    


    





    
    

