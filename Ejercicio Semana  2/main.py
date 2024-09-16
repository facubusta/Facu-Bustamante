from paquetes import calcular_impuestos, reportar_inf_empleado

horas_trabajadas = 40
antiguedad = 10
artefactos_producidos = 50

total_1 = calcular_impuestos(3500, 1000)
print(f"El resultado final es de: ${total_1}")

reportar_inf_empleado(horas_trabajadas, antiguedad, artefactos_producidos, "jose", 32)
