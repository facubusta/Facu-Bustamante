#3- Programar un algoritmo que permita crear una nueva lista de respondentes de manera
#secuencial. Deberán ingresar su nombre, sexo, cantidad de horas trabajadas e ingreso
#semanal en listas separadas

nombres = []
sexos = []
horas_trabajadas = []
ingresos_semanales = []


contador = 0
while True:
    nombre = input("Ingrese el nombre del respondente (o 'fin' para terminar): ")
    if nombre == 'fin': 
        break  
    
    sexo = input("Ingrese el sexo (M/F): ")
    horas = float(input("Ingrese la cantidad de horas trabajadas: "))
    ingreso = float(input("Ingrese el ingreso semanal: "))
    
   
    if contador >= len(nombres):
        nombres += [None] 
        sexos += [None]
        horas_trabajadas += [None]
        ingresos_semanales += [None]

    nombres[contador] = nombre
    sexos[contador] = sexo
    horas_trabajadas[contador] = horas
    ingresos_semanales[contador] = ingreso

    contador += 1
  
print(f"•Los nombres de la lista son: {nombres} \n•Los sexo son: {sexos} \n•Las horas trabajadas son: {horas_trabajadas} \n•Los ingresos semanales son: {ingresos_semanales}")




        

