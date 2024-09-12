def calcuar_factorial_r(n):
    
    if n > 0:
        resultado = n * calcuar_factorial_r(n-1)
        return resultado 
    else:
        return 1

print(calcuar_factorial_r(4))