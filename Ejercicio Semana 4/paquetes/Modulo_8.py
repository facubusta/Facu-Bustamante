#8- Desarrollar una función que verifique si todos los elementos de una lista son del mismo
#tipo. En ese caso que devuelva el tipo que contiene, en caso contrario que informe qué tipos
#de elementos contiene.


def verificar_tipos_lista(lista : list):
    '''Verifica los tipos de datos de la lista'''
    
    tipos_encontrados = [0] * len(lista)  
    cantidad_tipos = 0  

    for i in range(len(lista)):
        tipo_elemento = type(lista[i])
        es_repetido = False
        
        for j in range(cantidad_tipos):
            if tipos_encontrados[j] == tipo_elemento:
                es_repetido = True
                break
        
        if not es_repetido:
            tipos_encontrados[cantidad_tipos] = tipo_elemento 
            cantidad_tipos += 1  

    if cantidad_tipos == 1:
        return "Todos los elementos son del mismo tipo."

    tipos = ""
    for i in range(cantidad_tipos):
        if tipos_encontrados[i] == int:
            tipos += "int"
        elif tipos_encontrados[i] == float:
            tipos += "float"
        elif tipos_encontrados[i] == str:
            tipos += "str"

        if i < cantidad_tipos - 1:
            tipos += ", "

    return "La lista contiene los siguientes tipos: " + tipos








