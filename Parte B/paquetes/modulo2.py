from paquetes import modulo1

#Devuele el salario sumando la antiguedad
def calcular_salario(horas_trabajadas, antiguedad):
    salario = horas_trabajadas * 10
    incremento_antiguedad = modulo1.calcular_porcentaje(salario, 3 * antiguedad)
    salario_total = salario + incremento_antiguedad
    return salario_total

#Devuelve la productividad del empleado
def calcular_prod_empleado(artefactos_producidos, horas_trabajadas):
        if horas_trabajadas > 0:
            prod_empleado = artefactos_producidos / horas_trabajadas
            return prod_empleado 
        else:
             return 0   
        
#Muestra en pantalla toda la informacion del empleado
def reportar_inf_empleado(horas_trabajadas, antiguedad, artefactos_producidos, nombre : str, edad):
     salario = calcular_salario(horas_trabajadas, antiguedad)
     productividad = calcular_prod_empleado(artefactos_producidos, horas_trabajadas)
     print(f"La informacion del empleado es: \nNombre: {nombre}\nEdad: {edad}\nSalario: {salario}\nProductividad: {productividad}")







