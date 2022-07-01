from IsaacRamos_PGY1121_012_V_Funciones import menu
from IsaacRamos_PGY1121_012_V_Funciones import grabar
from IsaacRamos_PGY1121_012_V_Funciones import buscar
from IsaacRamos_PGY1121_012_V_Funciones import certificados
from IsaacRamos_PGY1121_012_V_Funciones import salida

menu()
x=int(input('Escriba acá su opción: '))
while x<=4:
    if x==1:
        grabar()
    elif x==2:
        buscar()
    elif x==3:
        certificados()
    else:
        salida()
    menu()
    x=int(input('Escriba acá su opción: '))
salida()