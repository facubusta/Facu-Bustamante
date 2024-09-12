#una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
#que en caso de no recibir un radio el valor del mismo será 3.

def calcular_radio_circulo(radio: float = 3) -> float:
    '''calcula el area de un circulo'''
    py = 3.14
    resultado = py * (radio * radio)
    return resultado

print(f"El area del circulo es de : {calcular_radio_circulo(30)}")

#b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
#parámetro, sin parámetros opcionales.

def calcular_area_cuadrado(lado : float) -> float:
    '''cualcula el area de un cuadrado'''
    resultado = lado * lado
    return resultado

print(f"El area del cuadrado es de : {calcular_area_cuadrado(2)}")

#C- una función que calcule el área de un triángulo recibiendo base y altura por parámetro.

def calcular_area_triangulo(base : float, altura : float) -> float:
    
    resultado = (base * altura) / 2  
    return resultado

print(f"El area del triangulo  es de : {calcular_area_triangulo(2, 4)}")
