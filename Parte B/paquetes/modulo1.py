# Devuelve el valor total sumando los impuestos
def calcular_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones = 15):
    resultado_nacional = valor_ventas_nacionales + calcular_porcentaje(valor_ventas_nacionales, iva)
    resultado_exportaciones = valor_exportaciones - calcular_porcentaje(valor_exportaciones, retenciones)
    resultado_final = resultado_nacional + resultado_exportaciones
    return resultado_final

# Devuelve el porcentaje
def calcular_porcentaje(importe, porcentaje):
    resultado = importe * porcentaje / 100
    return resultado