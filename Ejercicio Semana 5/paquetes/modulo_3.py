#5- Realizar una función que calcula la media de cualquier lista. Validar que lo que se recibe
#sean números.

def calcular_media(lista: list) -> float:
    '''Calcula la media de una lista'''

    suma_lista = 0
    cantidad_numeros = 0

    for num in lista:
        if type(num) == list: 
            for sub_num in num: 
                if type(sub_num) == float or type(sub_num) == int:
                    suma_lista += sub_num
                    cantidad_numeros += 1
                else:
                    print(f"'{sub_num}' no es un número y será ignorado.")
        elif type(num) == float or type(num) == int:
            suma_lista += num
            cantidad_numeros += 1
        else:
            print(f"'{num}' no es un número y será ignorado.")

    return suma_lista / cantidad_numeros


        

    
            

        