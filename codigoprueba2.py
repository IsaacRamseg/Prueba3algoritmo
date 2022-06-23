from resolutionprueba2 import menu
from resolutionprueba2 import registro_vehiculo
from resolutionprueba2 import mantenimiento
from resolutionprueba2 import consulta
from resolutionprueba2 import salida

menu()
x=int(input('Escriba acá su opción: '))
while x<=4:
    if x==1:
        registro_vehiculo()
    elif x==2:
        mantenimiento()
    elif x==3:
        consulta()
    else:
        salida()
    menu()
    x=int(input('Escriba acá su opción: '))
salida()
