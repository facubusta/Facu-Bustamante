#3
#Inicializar una matriz de 4 columnas y 4 filas. Cargar en cada cruce de fila y columna el
#valor correspondiente a la multiplicación del índice de fila y columna.

matriz_inicial =[[0] * 4, [0] * 4,[0] * 4, [0] * 4] 

for i in range(len(matriz_inicial)):
    for j in range(len(matriz_inicial)):
        matriz_inicial[i][j] = i * j

print(matriz_inicial)
     