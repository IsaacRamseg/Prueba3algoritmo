import numpy as np
from os import system

class Funciones():

    compradores = []
    asientos = np.array(range(1, 43), dtype="str")

    def limpiaPantalla(self):
        system("cls")

    def formatoValor(self, valor):
        if len(valor) < 2:
            return f" {valor}"
        return valor

    def generaMenu(self):
        return ["1. Ver asientos disponibles","2. Comprar asiento","3. Anular vuelo","4. Modificar datos de pasajero", "5. Mostrar Compras","6. Salir"]

    def mostrarAsientosDisponibles(self):
        
        filaAsientos = np.array_split(self.asientos, 7)
        for index, filaAsiento in enumerate(filaAsientos):
            if index == 5:
                print("|", "__", "__", "__", "        ", "__", "__", "__", "|")
                print("|", "__", "__", "__", "        ", "__", "__", "__", "|")
            
            print("|", self.formatoValor(filaAsientos[index][0]), self.formatoValor(filaAsientos[index][1]), self.formatoValor(filaAsientos[index][2]), "        ", self.formatoValor(filaAsientos[index][3]), self.formatoValor(filaAsientos[index][4]), self.formatoValor(filaAsientos[index][5]), "|")

    def mostrarAsientos(self):
        
        filaAsientos = np.array_split(self.asientos, 7)
        for index, filaAsiento in enumerate(filaAsientos):
            if index == 5:
                print("|", "__", "__", "__", "        ", "__", "__", "__", "|")
                print("|", "__", "__", "__", "        ", "__", "__", "__", "|")
            
            print("|", self.formatoValor(filaAsientos[index][0]), self.formatoValor(filaAsientos[index][1]), self.formatoValor(filaAsientos[index][2]), "        ", self.formatoValor(filaAsientos[index][3]), self.formatoValor(filaAsientos[index][4]), self.formatoValor(filaAsientos[index][5]), "|")

        input("Presione cualquier tecla para continuar...")
        self.limpiaPantalla()

    def compraBoletos(self):

        while True:
            self.mostrarAsientosDisponibles()
            print("")
            print("x => asiento ocupado")
            print("Asientos normal = por $78.900")
            print("Asientos VIP = del 31 al 42 por $240.000")
            asiento = int(input("Seleccione un asiento disponible: "))
            asientoSeleccionado = self.asientos[asiento - 1]
            valor = 78900
            if asientoSeleccionado in ["31","32","33","34","35","36","37","38","39","40","41","42"]:
                valor = 240000
            
            if asientoSeleccionado == "x":
                self.limpiaPantalla()
                print("El asiento seleccionado se encuentra ocupado por favor seleccione otro")
            else:
                opcion = int(input(f"El asiento {asientoSeleccionado} tiene un valor de ${valor}, ¿desea continuar? 1: Sí 2: no "))
                if opcion == 1:
                    self.limpiaPantalla()
                    descuento = 0
                    nombres = input("Ingrese su nombre y apellido: ")
                    run = input("Ingrese RUN sin puntos ni guion: ")
                    telefono = input("Ingrese su telefono: ")
                    banco = int(input("Seleccione banco 1: Santander 2: bancoDuoc 3: Chile "))
                    if banco == 2:
                        print("Se aplicara un 15% de descuento")
                        descuento = 0.15
                    
                    print(f"Total: {valor - (valor * descuento)}")
                    self.asientos[asiento - 1] = "x"
                    self.compradores.append([asientoSeleccionado, nombres, run, telefono, banco])
                    input("¡Boleto comprado!, muchas gracias, presione cualquier tecla para continuar....")
                    self.limpiaPantalla()
                    break
                else:
                    self.limpiaPantalla()
                    break
    
    def anulaPasaje(self):
        run = input("Ingrese RUN sin puntos ni guion: ")
        asiento = input("Ingrese asiento comprado: ")
        encontrado = False

        for comprador in self.compradores:
            if run in comprador:
                if asiento == comprador[0]:
                    encontrado = True

        if encontrado:
            self.asientos[int(asiento) - 1] = asiento
            input("Se ha anulado la compra, presione cualquier tecla para continuar....")
            self.limpiaPantalla()
        else:
            input("No se ha encontrado la compra, presione cualquier tecla para continuar....")
            self.limpiaPantalla()

    def modificaBoleto(self):
        runBusqueda = input("Ingrese RUN sin puntos ni guion: ")
        asiento = input("Ingrese asiento comprado: ")
        encontrado = False
        indice = 0

        #[asientoSeleccionado, nombres, run, telefono, banco]

        for index, comprador in enumerate(self.compradores):
            if runBusqueda in comprador:
                if asiento == comprador[0]:
                    encontrado = True
                    indice = index

        if encontrado:
            nombreNuevo = input("Ingrese nombre nuevo del pasajero: ")
            telefonoNuevo = input("Ingrese telefono nuevo del pasajero: ")
            asientoSeleccionado, nombres, run, telefono, banco = self.compradores[indice]
            self.compradores[indice] = [asientoSeleccionado, nombreNuevo, run, telefonoNuevo, banco]
            input("Se ha modificado la compra, presione cualquier tecla para continuar....")
            self.limpiaPantalla()
        else:
            input("No se ha encontrado la compra, presione cualquier tecla para continuar....")
            self.limpiaPantalla()

    def mostrarCompradores(self):
        print(self.compradores)
        input("Presione cualquier tecla para continuar....")
        self.limpiaPantalla()

import numpy as np
from utils.funciones import Funciones

funcs = Funciones()

while True:

    for item in funcs.generaMenu():
        print(item)

    opcion = int(input("Seleccione un item del menu: "))
    if opcion == 1:
        funcs.mostrarAsientos()
    if opcion == 2:
        funcs.compraBoletos()
    if opcion == 3:
        funcs.anulaPasaje()
    if opcion == 4:
        funcs.modificaBoleto()
    if opcion == 5:
        funcs.mostrarCompradores()
    if opcion == 6:
        funcs.limpiaPantalla()
        break
        