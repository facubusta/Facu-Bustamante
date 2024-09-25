#9- Desarrollar una función que permita cargar nuevos valores a una lista cualquiera. Se
#debe poder validar el tipo de datos que contiene la lista.

def cargar_valor(lista, nuevo_valor):
    '''Permite cargar un valor a una lista siempre y caundo sea del mismo tipo'''
    if not lista:
        return f"Se puede agregar {nuevo_valor} a la lista vacía."
    
    tipo_lista = type(lista[0])
    
    if type(nuevo_valor) == tipo_lista:
        return f"Valor {nuevo_valor} validado y listo para ser agregado a la lista."
    else:
        return f"Error: El valor {nuevo_valor} no es del tipo {tipo_lista.__name__}."


