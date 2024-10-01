#4- Dadas las siguientes listas anidadas:
#nombres = [“Juan”, “Ricardo”, “Nahuel”, “Eugenia”, “Jimena”]
#edades = [23, 35, 34, 40, 24]
#géneros = [“Hombre”, “Hombre”, “Hombre”, “Mujer”, “Mujer”]
#a) Calcular media etaria para hombres y mujeres

nombres = ["Juan", "Ricardo", "Nahuel", "Eugenia", "Jimena"]
edades = [23, 35, 34, 40, 24]
géneros = ["Hombre", "Hombre", "Hombre", "Mujer", "Mujer"]

cant_hombres = 0
cant_mujeres = 0
edad_hombres = 0
edad_mujeres = 0
nombres_hombres = [] 
nombres_mujeres = [] 

for i in range(len(edades)):
    if géneros[i] == "Hombre":
        edad_hombres += edades[i]
        cant_hombres += 1
        nombres_hombres = nombres_hombres + [nombres[i]] 
    else:
        edad_mujeres += edades[i]
        cant_mujeres += 1
        nombres_mujeres = nombres_mujeres + [nombres[i]]

media_etaria_hombres = edad_hombres / cant_hombres
media_etaria_mujeres = edad_mujeres / cant_mujeres

print(f"La media etaria para hombres es de: {media_etaria_hombres} y sus nombres son: {nombres_hombres}")
print(f"La media etaria para mujeres es de: {media_etaria_mujeres} y sus nombres son {nombres_mujeres}")
        






