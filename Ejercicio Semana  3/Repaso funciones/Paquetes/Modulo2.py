#2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
#de las mismas figuras que el punto 1.

def calcular_perimetro_circulo(diametro : float) ->float:
    '''Calcula el perimetro de un circulo'''
    py = 3.14
    resultado = py * diametro 
    return resultado

print(f"El perimetro del un circulo es : {calcular_perimetro_circulo(20)}")

def calcular_perimetro_cuadrado(lado : float) ->float:
    '''Calcula el perimetro de un cuadrado'''
    resultado = lado * 4
    return resultado

print(f"El perimetro del un cuadrado es : {calcular_perimetro_cuadrado(20)}")

def calcular_perimetro_triangulo(lado_a: float, lado_b: float, lado_c : float) ->float:
    '''Calcula el perimetro de un triangulo'''
    resultado = lado_a + lado_b + lado_c
    return resultado

print(f"El perimetro del un triangulo es : {calcular_perimetro_triangulo(20, 50.3, 102454.3)}")
