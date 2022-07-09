import numpy as np
from os import system
from datetime import datetime

audiencia = []
butacas = np.array(range(1, 101), dtype="str")

def limpiar_pantalla():
    system("cls")

def menu():
    print('1. Comprar entradas \n2. Mostrar ubicaciones disponibles \n3. Ver listado de asistentes \n4. Mostrar ganancias totales \n5. Salir') 


def mostrar_butacas():
    print(butacas)
    input("Las butacas ocupadas aparecen con una x, el resto están disponibles. Presione enter para continuar.")
    limpiar_pantalla()

def comprar_entradas():
    global platinum
    global gold
    global silver
    platinum=0
    gold=0
    silver=0
    while True:
        print("Asientos Platinum, $120.000. (Asientos del 1 al 20)")
        print("Asientos Gold, $80.000. (Asientos del 21 al 50) ")
        print("Asientos Silver, $50.000. (Asientos del 51 al 100)")
        ubicacion = int(input("Seleccione una butaca disponible: "))
        butaca_ubicacion = butacas[ubicacion - 1]
        if butaca_ubicacion in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]:
            valor = 120000
            platinum+=1
        elif butaca_ubicacion in ["21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50",]:
            valor = 80000
            gold+=1
        else:
            valor=50000
            silver+=1    
        if butaca_ubicacion == "x":
            limpiar_pantalla()
            print("La butaca seleccionada se encuentra ocupada por favor seleccione otra")
        else:
            op = int(input(f"El asiento {butaca_ubicacion} tiene un valor de ${valor}, ¿desea continuar? 1: Sí 2: no "))
            if op == 1:
                limpiar_pantalla()
                run = input("Ingrese RUN sin puntos ni guion ni dígito verificador: ")                    
                print(f"Total: {valor}")
                butacas[ubicacion - 1] = "x"
                audiencia.append([run,butaca_ubicacion])
                input("¡Boleto comprado!, muchas gracias, presione enter para continuar.")
                limpiar_pantalla()
                break
            else:
                limpiar_pantalla()
                break
    

def lista_asistentes():
    print(audiencia)

def ganancias():
    totplatinum=platinum*120000
    totgold=gold*80000
    totsilver=silver*50000
    print('   Tipo de entrada   ','   ','   Cantidad   ','   ','   Total   ')
    print('  Platinum $120.000  ','        ',platinum,'        ',totplatinum)
    print('  Gold     $ 80.000  ','        ',gold,'              ',totgold)
    print('  Silver   $ 50.000  ','        ',silver,'           ',totsilver)

def salida():
    print('Hasta luego. Atentamente Isaac Ramos.',datetime.today())