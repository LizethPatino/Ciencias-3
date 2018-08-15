# -*- coding: utf-8 -*-
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]
        self.limiteEspacios = 30

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        if self.limiteEspacios > 1:
            self.items.append(x)
            self.limiteEspacios-=1

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            if self.limiteEspacios<30:
                self.limiteEspacios+=1
            return self.items.pop(0)
        except IndexError:
            raise ValueError("El parqueadero esta vacio")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

    def mostrar(self):
        for Persona in self.items:
            print('\t'+Persona.mostrarDatos())

class Persona:
    """ Representa el contenedor de los datos: CodEst, Nombre y placa
    vehiculo"""

    def __init__(self,x ,y ,z):
        """ Inicializador de persona """
        self.codigo = x
        self.nombre = y
        self.placa  = z

    def getNombre(self):
        return self.nombre

    def getCodigo(self):
        return self.codigo

    def getPlaca(self):
        return self.placa

    def mostrarDatos(self):
        return self.getCodigo() +' '+ self.getNombre() +' '+ self.getPlaca()

# -*- coding: cp1252 -*-
def anadir(cola):
    codigo = input('ingrese el codigo de la persona: ')
    nombre = input('ingrese el nombre de la persona: ')
    placa = input('ingrese la placa del vehiculo: ')
    cola.encolar(Persona(codigo, nombre, placa))
    
def pedirNumeroEntero(): 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num