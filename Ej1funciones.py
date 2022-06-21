import math
def menu():
    print('Ingrese una opcion:')
    print('1. Verificar Numero primo')
    print('2. Calcular Factorial')
    print('3. Verificar Palíndrome')
    print('4. Salir del programa')

def num_primo():
    primo=int(input('Ingrese un numero entre 1 y 15:'))
    if primo%2 == 0:
        print('Numero es compuesto')
    else:
        print('Numero es primo')
 
def factori():
    factor=int(input('Ingrese un numero entre 3 y 10:'))
    calcu_fact= math.factorial(factor)
    print(calcu_fact)

def palindrome():
    lista=list()
    palabra=input('Ingrese una palabra para verificar si es palíndrome: ')
    for l in palabra:
        lista.append(l)
    if lista[::-1]==lista:
        print('Tu palabra es palindrome')
    else:
        print('tu palabra no es palindrome')

def salida():
    print('Hasta luego. Atentamente Isaac Ramos.')