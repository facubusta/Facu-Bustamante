#1 - Calcular mediante recursividad la potencia de un número, mediante una función que
#recibe un número base de tipo entero y un exponente de tipo entero. Utilizar parámetros
#opcionales para definir que si la función no recibe ningún parámetro devolverá 2 al cuadrado.

def calcular_potencia_numero(base : int = 2, expo : int = 2) ->int:
    '''Calcula la potencia de base y exponente'''
    if expo == 0:
        return 1
    elif expo == 1:
        return base
    elif expo > 1:
        return base * calcular_potencia_numero(base, expo - 1)
    elif expo < 0:
        return 1 / calcular_potencia_numero(base, -expo)

base = 10
expo = -4
print(f"El resultado de calcular {base} por {expo} es de :  {calcular_potencia_numero(base, expo)}")