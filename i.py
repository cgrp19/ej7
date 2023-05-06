import os
import csv
from claseViajeroFrec import ViajeroFrec as vf

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            0: self.salir
                        }
        
    def opcion(self,op, mPA):   ##mPA == manejador plan de ahorro
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op ==1 or op==2 or op==3 or op==4:
            func(mPA)
        else:
            func()

    def buscarViajero (self, n, xLV):
        indice=0
        valorDeRetorno = None
        bandera=False
        while not bandera and indice < len(xLV):
            if xLV[indice].getNumero()==n:
                bandera=True
                valorDeRetorno=indice
            else: indice+=1
        if valorDeRetorno == None:
            print ('Error, Numero no encontrado')
        return valorDeRetorno

    def mostrarMenu(self, xLV=None):
        os.system('cls')
        print ('''
    -------->Menu<--------
    Seleccione una opcion:
    1. Realizar carga
    2. Hacer comparacion por izq y der (inciso 1)
    3. Acumular millas (inciso 2)
    4. Canjear millas (inciso 3)
    0. Salir
''')
    def comparaPorIzq (self, xLV): ## Compara con la primera instancia de Viajero Frecuente
        os.system('cls')
        print ('-------->igual por Izquierda<--------')
        x = int (input ('Ingrese cantidad de millas a comparar: '))
        if xLV[0] == x:
            print ('Son Iguales')
        else: print ('Son distintos')
    
    def comparaPorDer (self, xLV):
        print ('-------->igual por Derecha<--------')
        x = int (input ('Ingrese cantidad de millas a comparar: '))
        if x == xLV[0]:
            print ('Son Iguales')
        else: print ('Son distintos')

## OPCIONES

    def opc1 (self, xLV):
        total = 0
        bandera = True
        path = './Viajeros.csv'
        archivo = open(path, 'r')
        reader = csv.reader(archivo, delimiter =',')
        for fila in reader:
            if bandera:
                bandera = False
            else:
                xNum = int (fila[0])
                xDNI = fila[1]
                xNombre = fila[2]
                xApellido = fila[3]
                xMillas = int (fila[4])
                viajero = vf(xNum, xDNI, xNombre, xApellido, xMillas)
                xLV.append(viajero)
                total += 1
        if total > 0:
            print (f'Lista cargada correctamente, se cargaron {total} viajeros')
        else:
            print ('Error en la carga')

    def opc2 (self, xLV):
        os.system('cls')
        self.comparaPorIzq(xLV)
        self.comparaPorDer(xLV)
        

    def opc3 (self, xLV):
        os.system('cls')
        r = int (input ('Ingrese numero de viajero: '))
        i = self.buscarViajero(r, xLV)
        x = int (input ('Ingrese millas a acumular: '))
        xLV[i] = x + xLV[i]
        print (f'Cantidad de millas actuales: {xLV[i].getMillas()}')

    def opc4 (self, xLV):
        os.system('cls')
        r = int (input ('Ingrese numero de viajero: '))
        i = self.buscarViajero(r, xLV)
        x = int (input ('Ingrese millas a canjear: '))
        xLV[i] = x - xLV[i]
        print (f'Cantidad de millas actuales: {xLV[i].getMillas()}')

    def salir (self):
        print ('saliendo...')