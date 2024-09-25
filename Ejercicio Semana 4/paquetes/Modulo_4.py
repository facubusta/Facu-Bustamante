#4)Desarrollar una función que calcule la media de ingresos por cuartil.

def  calcular_media_por_cuartil(ingresos : list):
    '''Calcula la media por cuartil'''
   
    n = len(ingresos)
    
    cuartil_uno = n // 4
    cuartil_dos = n // 2
    cuartil_tres= (3 * n) // 4

    sumas = [0, 0, 0, 0]
    contadores = [0, 0, 0, 0]

    
    for ingreso in ingresos:
        if ingreso <= ingresos[cuartil_uno]:  
            sumas[0] += ingreso
            contadores[0] += 1
        elif ingreso <= ingresos[cuartil_dos]: 
            sumas[1] += ingreso
            contadores[1] += 1
        elif ingreso <= ingresos[cuartil_tres]:
            sumas[2] += ingreso
            contadores[2] += 1
        else: 
            sumas[3] += ingreso

            contadores[3] += 1

    medias = [0, 0, 0, 0]
    for i in range(4):
        if contadores[i] > 0:
            medias[i] = sumas[i] / contadores[i]

    return { 'Media Cuartil 1': medias[0],
             'Media Cuartil 2': medias[1],
             'Media Cuartil 3': medias[2],
            'Media Cuartil 4': medias[3] }


    





   








    

    
    
    