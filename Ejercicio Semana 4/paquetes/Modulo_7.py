def buscar_menores(nombres, edades):
    '''Busca en una lista la o las personas de menor edad'''
    
    menor_edad = edades[0]
    for edad in edades:
        if edad < menor_edad:
            menor_edad = edad

    cantidad_menores = 0  
    menores = [0] * len(edades)  

    for i in range(len(edades)):
        if edades[i] == menor_edad:
            menores[cantidad_menores] = (nombres[i], edades[i])  
            cantidad_menores += 1  

    
    print("Personas de menor edad:")
    for nombre, edad in menores[:cantidad_menores]:
        if nombre:  # Verifica que el nombre no esté vacío
            print(f"{nombre}: {edad} años")


nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]



