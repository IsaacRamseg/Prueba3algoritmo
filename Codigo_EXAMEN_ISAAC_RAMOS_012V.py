from Funciones_EXAMEN_ISAAC_RAMOS_012V import limpiar_pantalla
from Funciones_EXAMEN_ISAAC_RAMOS_012V import menu
from Funciones_EXAMEN_ISAAC_RAMOS_012V import mostrar_butacas
from Funciones_EXAMEN_ISAAC_RAMOS_012V import comprar_entradas
from Funciones_EXAMEN_ISAAC_RAMOS_012V import lista_asistentes
from Funciones_EXAMEN_ISAAC_RAMOS_012V import ganancias
from Funciones_EXAMEN_ISAAC_RAMOS_012V import salida

menu()
x=int(input('Ingrese acá su opción: '))
while x != 5:
    if x==1:
        mostrar_butacas()
        comprar_entradas()
    elif x==2:
        mostrar_butacas()
    elif x==3:
        lista_asistentes()
    elif x==4:
        ganancias()
    else:
        salida()
        break
    menu()
    x=int(input('Ingrese acá su opción: '))
salida()