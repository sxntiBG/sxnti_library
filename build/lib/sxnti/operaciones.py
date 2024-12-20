def Sumar(*args):
    return sum(args)

def Restar(*args):
    if not args:
        raise ValueError("No hay argumentos para restar")
    
    resultado = args[0]
    for num in args[1:]:
        resultado -= num
    return resultado

def Multiplicar(*args):
    if not args:
        raise ValueError("No hay argumentos para multiplicar")
    
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def Dividir(*args):
    if not args:
        raise ValueError("No hay argumentos para dividir")
    
    resultado = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("No se puede dividir por cero")
        resultado /= num
    return resultado
