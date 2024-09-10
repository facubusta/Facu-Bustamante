from paquetes import modulo1
from paquetes import modulo2

horas_trabajadas = 40
antiguedad = 10
artefactos_producidos = 50

total_1 = modulo1.calcular_impuestos(1000, 1000)
print(f"El resultado final es de: ${total_1}")

modulo2.reportar_inf_empleado(horas_trabajadas, antiguedad, artefactos_producidos, "jose", 32)
