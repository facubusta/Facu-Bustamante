def calcular_nacional(valor_ventas_nacionales, iva = 21)->float:
    ''' Devuelve el valor total nacional'''
    resultado_nacional = valor_ventas_nacionales * (1 / (1 + (iva / 100)))
    return resultado_nacional

def calcular_exportaciones(valor_exportaciones, retenciones = 15)->float:
    ''' Devuelve el valor total exportado'''
    resultado_exportaciones = valor_exportaciones * (1 - (retenciones / 100))
    return resultado_exportaciones

def calcular_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones = 15):
    ''' Devuelve el valor total de ventas'''
    total_calculo = calcular_exportaciones(valor_exportaciones, retenciones) + calcular_nacional(valor_ventas_nacionales, iva)
    return total_calculo