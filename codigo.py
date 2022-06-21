from Ej1funciones import menu
from Ej1funciones import num_primo
from Ej1funciones import factori
from Ej1funciones import palindrome
from Ej1funciones import salida
menu()
x=int(input('Escriba su opción:'))
if x==1:
    num_primo()
elif x==2:
    factori()
elif x==3:
    palindrome()
elif x==4:
    salida()
else:
    print('Por favor ingrese una opción válida')
print('Hasta luego. Atentamente Isaac Ramos')