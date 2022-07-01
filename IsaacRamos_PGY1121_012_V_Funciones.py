import random
def menu():
    print('Bienvenido a Auto Seguro ¿que desea hacer?')
    print('1. Grabar datos de un vehículo')
    print('2. Buscar información de un vehículo')
    print('3. Imprimir certificados')
    print('4. Salir')

def grabar():
    global vehiculo
    global patente
    global marca
    global precio
    global nom_dueno
    patente=list()
    marca=list()
    precio=list()
    nom_dueno=list()
    while True:
        xpat=input('Ingrese patente (ej: XXXX-00): ')   
        if len(xpat)==7 and ((xpat[0:4].isalpha() and xpat[5:7].isdigit())):
            xprecio=int(input('Ingrese precio del vehículo (Obs: Sin el signo $): '))
            if xprecio>1000000:
                xmar=input('Ingrese marca: ')    
                if len(xmar)>=2 and len(xmar)<=15:
                    xnom=input('Ingrese nombre del dueño: ')
                    if xnom != "":
                        input('Datos ingresados exitosamente! \nPresione cualquier tecla para continuar')
                        break
                    else:
                        input('Debe ingresar un dueño, \nPresione cualquier tecla para continuar')
                else:
                    input('Debe ingresar marca, \nPresione cualquier tecla para continuar')
            else:
                input('Ingrese un precio válido, \nPresione cualquier tecla para continuar')
        else:
            input('Ingrese una patente válida, \nPresione cualquier tecla para continuar')    
    patente.append(xpat); marca.append(xmar); precio.append(xprecio); nom_dueno.append(xnom)
    vehiculo=[patente,marca,precio,nom_dueno]
    return vehiculo

def buscar():
    xpat=input('Ingrese la patente del vehículo que quiere buscar:')
    i=patente.index(xpat)
    if xpat not in patente:
        input('Vehículo no encontrado en la base de datos, \nPresione cualquier tecla para continuar')
    print(f'{vehiculo[0][i]} \n {vehiculo[1][i]} \n {vehiculo[2][i]} \n {vehiculo[3][i]}')

def certificados():
    xpat=input('Ingrese la patente del vehículo que quiere revisar:')
    i=patente.index(xpat)
    print('¿Que certificado le gustaría revisar')
    print('1. Certificado de antecedentes (multas)')
    print('2. Emisión de gases')
    print('3. Anotaciones vigentes')
    print('4. Salir')
    x=input('Ingrese acá su opción, luego presione enter: ')
    while True:
        if x=='1': 
            antecedentes=random.randint(0,3501)
            print('Certificado de antecedentes ',' $',antecedentes,' ' ,vehiculo[0][i],' ', vehiculo[3][i])
            break
        elif x=='2': 
            antecedentes=random.randint(0,3501)
            print('Emision de gases ',' $',antecedentes,' ' ,vehiculo[0][i],' ', vehiculo[3][i])
            break
        elif x=='3': 
            antecedentes=random.randint(0,3501)
            print('Anotaciones vigentes ',' $',antecedentes,' ' ,vehiculo[0][i],' ', vehiculo[3][i])
            break
        else:
            input('Ha salido del menú de certificados, pulse cualquier tecla para continuar')
            break

def salida():
    print('Cerrando Sesión \nIsaac Ramos \nProgramaV1.1')

