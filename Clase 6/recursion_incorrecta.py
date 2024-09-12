def imprimir_n(n: int)-> int:
    if n > int(-998):
        imprimir_n(n-1)
        print(n)

imprimir_n(0)