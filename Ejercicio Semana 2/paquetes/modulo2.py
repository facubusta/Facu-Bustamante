def calcular_salario(horas_trabajadas, antiguedad)->float:
    '''Devuele el salario sumando la antiguedad'''  
    salario = horas_trabajadas * 10
    incremento_antiguedad = salario * (3*antiguedad)/100
    salario_total = salario + incremento_antiguedad
    return salario_total

def calcular_prod_empleado(artefactos_producidos, horas_trabajadas)->float:
    '''Devuelve la productividad del empleado'''
    if horas_trabajadas > 0:
        prod_empleado = artefactos_producidos / horas_trabajadas
        return prod_empleado 
    else:
        return 0   
        
def reportar_inf_empleado(horas_trabajadas, antiguedad, artefactos_producidos, nombre : str, edad)->str:
     '''Muestra en pantalla toda la informacion del empleado'''
     salario = calcular_salario(horas_trabajadas, antiguedad)
     productividad = calcular_prod_empleado(artefactos_producidos, horas_trabajadas)
     print(f"La informacion del empleado es: \nNombre: {nombre}\nEdad: {edad}\nSalario: {salario}\nProductividad: {productividad}")







