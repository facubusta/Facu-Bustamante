def calcular_mov_torres(discos: int, torre_inicio: str, torre_final: str, torre_aux: str) -> None:
    '''Calcula los movimientos que debemos hacer para ganar'''
    if discos == 1:
        print(f"Mover el disco 1 de la torre {torre_inicio} a la torre {torre_final}")
    else:
        calcular_mov_torres(discos - 1, torre_inicio, torre_aux, torre_final)
        print(f"Mover e disco {discos} de la torre {torre_inicio} a la torre {torre_final}")
        calcular_mov_torres(discos - 1, torre_aux, torre_final, torre_inicio)
        
discos = 3
calcular_mov_torres(discos, "A", "B", "C")





