'''Supongamos que está trabajando en desarrollar el programa de carga de una encuesta.
1 - Pedir al usuario que ingrese nombre y apellido del encuestado, guardarlo como string.
2 - Pedir al usuario que ingrese el salario mensual del encuestado y guardarla como entero.
3 - Pedir al usuario que ingrese la cantidad de horas trabajadas en la semana anterior por el
encuestado y guardarlo como entero. Validar que sea un valor entre 0 y 120
4 - Calcular el ingreso horario del encuestado (ingreso dividido por horas trabajadas) y
generar una respuesta por pantalla con todos los datos ingresados para verificar que estén
bien cargados.'''


'''nombre_y_apellido = str(input("Por favor ingrese su nombre y apellido : "))
salario_mensual = int(input("Por favor ingrese su salario mensual : "))
cant_horas_trabajadas = int(input("Por favor ingrese las horas trabajadas la semana anterior : "))
while cant_horas_trabajadas < 0 or cant_horas_trbajadas > 120:
    cant_horas_trbajadas = int(input("Por favor ingrese correctamente la horas trabajadas entre 0 y 120 : "))
ingreso_horario = round(float((salario_mensual / cant_horas_trabajadas)))

print(f"Su nombre es : {nombre_y_apellido}")
print(f"Su salario es de : {salario_mensual}")
print(f"Las horas trabajadas es de : {cant_horas_trabajadas}")
print(f"Su ingreso horario es de : {ingreso_horario}")'''

'''5 - Dada la siguiente lista de ingresos horarios:
[ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
a) Calcular el promedio de ingresos/hora del 20% que más gana.
b) Calcular el promedio de ingresos/hora de todos los respondentes.
c) Buscar cuál es el valor que más se repite.
d) Calcular la media geométrica'''

'''ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]

porcentaje_20 =((len(ingresos) * 0.20))

maximo_1 = ingresos[0]
for numero in ingresos:
    if numero > maximo_1:
        maximo_1 = numero
maximo_2 = ingresos[0]
for numero in ingresos:
    if numero > maximo_2 and maximo_1 > numero:
        maximo_2 = numero
maximo_3 = ingresos[0]
for numero in ingresos:
    if numero > maximo_3 and maximo_2 > numero:
        maximo_3 = numero
maximo_4 = ingresos[0]
for numero in ingresos:
    if numero > maximo_4 and maximo_3 > numero:
        maximo_4 = numero

promedio = float((maximo_1 + maximo_2 + maximo_3 + maximo_4) / porcentaje_20)


print(f"El 20% de ingresos que hay es de : {porcentaje_20}")
print(f"Los numeros maximos son {maximo_1}, {maximo_2}, {maximo_3} y {maximo_4}")
print(f"El promedio es de : {promedio}")'''


#B
'''ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]
total = 0
for numeros in ingresos:
    total += numeros
    
promedio_todos = total / len(ingresos)

promedio_todos = sum(ingresos) / len(ingresos)
print(f"El promedio de ingresos/hora de todos los respondentes es de : {promedio_todos}")'''

#C
ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]
conteo = 0
num_repetido = 0
num_repetido_aux = 0
numero = 0 

for numeros in ingresos:
    conteo = numeros
    for num in ingresos:
        if conteo == num:
            num_repetido_aux += 1
    
    if num_repetido_aux > num_repetido:
        num_repetido = num_repetido_aux
        numero = numeros
    
    num_repetido_aux = 0

print(numero)

#D
'''ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]
total = 1

for num in ingresos:
    total = total * num


print(round(total ** (1/len(ingresos)), 3))'''


