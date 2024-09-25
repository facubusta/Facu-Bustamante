lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", "Daniel", "Jimena", "Mariela", "Ignacio"]

#A
edad_mas_joven = float('inf')
nombre_mas_joven = 0
edad_mas_grande = 0
nombre_mas_grande = 0

for i in range(len(lista_edad)):
    if lista_edad[i] < edad_mas_joven:
        edad_mas_joven = lista_edad[i]
        nombre_mas_joven = lista_nombres[i]

    if lista_edad[i] > edad_mas_grande:
        edad_mas_grande = lista_edad[i] 
        nombre_mas_grande = lista_nombres[i] 

print(f"El Nombre mas joven es {nombre_mas_joven} con {edad_mas_joven} años \nEl nombre mas grade es {nombre_mas_grande} con {edad_mas_grande} años.")

#B
for edad in lista_edad:
    if edad > 65:
        print("Se encontró una persona mayor de 65 años.")
        break
else:
    print("No hay personas mayores de 65 años.")

#C
suma_edades = 0
contador = 0

for edad in lista_edad:
    if edad <= 40:
        continue
    suma_edades += edad
    contador += 1

media_etaria = suma_edades / contador
print(f"La media etaria de edades mayores a 40 años es de {media_etaria}")





