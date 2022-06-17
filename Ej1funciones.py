import math
def menu():
    print('Seleccione una opcion:')
    print('1. Ingrese un numero entre 1 y 15, para verificar si es primo')
    print('2. Ingrese un numero entre 3 y 10 para calcular su factorial')
    print('3. Ingrese una frase para identificar si es palíndrome o no')
    print('4. Salir del programa')

def num_primo():
    primo=int(input('Ingrese un numero entre 1 y 15:'))
    if primo%2 == 0:
        print('Numero es compuesto')
    else:
        print('Numero es primo')
 

def factorial():
    factor=int(input('Ingrese un numero entre 1 y 15:'))
    calcu_fact= math.factorial(factor)
    return calcu_fact

def palindrome():
    

