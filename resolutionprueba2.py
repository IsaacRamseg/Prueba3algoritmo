def menu():
    print('Bienvenido a ServiExpress ¿que desea hacer?')
    print('1. Registrar Vehículo')
    print('2. Registro de mantenimiento')
    print('3. Consultar Automóvil')
    print('4. Salir')

def registro_vehiculo():
    global vehiculo
    global patente
    global marca
    global modelo
    global ano_fab
    global tipo
    patente=list()
    marca=list()
    modelo=list()
    ano_fab=list()
    tipo=list()
    while True:
        xpat=input('Ingrese patente: ')   
        if len(xpat)==6 and ((xpat[0:4].isalpha() and xpat[4:6].isdigit()) or (xpat[:2].isalpha() and xpat[2:6].isdigit())):
            xanio=int(input('Ingrese año de fabricación: '))
            if xanio>1900 and xanio<2021:
                xtipo=input('Ingrese tipo de vehículo: \n B-> Bencinero \n D-> Diesel \n E-> Eléctrico \n H-> Híbrido: ')
                if xtipo.lower()=='b' or xtipo.lower()=='d' or xtipo.lower()=='e' or xtipo.lower()=='h':
                    xmar=input('Ingrese marca: ')    
                    if xmar != "":
                        xmod=input('Ingrese modelo: ')
                        if xmod != "":
                            input('Datos ingresados exitosamente! \nPresione cualquier tecla para continuar')
                            break
                        else:
                            input('Debe ingresar modelo \nPresione cualquier tecla para continuar')
                    else:
                        input('Debe ingresar marca \nPresione cualquier tecla para continuar')
                else:
                    input('Ingrese un tipo válido \nPresione cualquier tecla para continuar')
            else:
                input('Ingrese un año válido \nPresione cualquier tecla para continuar')
        else:
            input('Ingrese una patente válida \nPresione cualquier tecla para continuar')    
    patente.append(xpat); marca.append(xmar); modelo.append(xmod); ano_fab.append(xanio); tipo.append(xtipo)
    vehiculo=[patente,marca,modelo,ano_fab,tipo]
    return vehiculo

def mantenimiento():
    registro=list()
    xreg=input('Ingrese nuevo registro de automóvil: ')
    registro.append(xreg)
    vehiculo.append(registro)
    print('Registro agregado exitosamente!')

def consulta():
    xpat=input('Ingrese la patente que quiere verificar:')
    i=patente.index(xpat)
#    if xpat not in patente:
#        input('Si desea agregar el vehículo presione cualquier tecla')

    print(f'{vehiculo[0][i]} \n {vehiculo[1][i]} \n {vehiculo[2][i]} \n {vehiculo[3][i]} \n {vehiculo[4][i]}')# \n {vehiculo[5][i]}')

def salida():
    print('Cerrando Sesión')
    