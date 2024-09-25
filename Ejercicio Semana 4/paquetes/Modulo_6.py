#6 - Desarrollar una función que pida 10 números dentro de un rango especificado, validar
#los números solicitados dentro de ese rango, guardar en una lista y retornarla. El programa
#principal debe invocar a la función y mostrar por pantalla el retorno.

def solicitar_numeros(rango_inferior, rango_superior) ->list:
    '''Solicita 10 numeros y retorna una lista'''

    numeros = [0] * 10  
    for i in range(10):
        while True:
            numero_str = input(f"Ingrese un número entre {rango_inferior} y {rango_superior}: ")
            
            numero = float(numero_str)  
            if rango_inferior <= numero <= rango_superior:
                numeros[i] = numero  
                break
            else:
                print(f"Error: Debe estar entre {rango_inferior} y {rango_superior}.")
    return numeros


