from motos import *

miCola = Cola()
salir = False
opcion = 0
 
while not salir:
    print ("1. agregar un motociclista")
    print ("2. salir del parqueadero")
    print ("3. Mostrar parqueaderos")
    print ("4. Salir")
    print ("Elige una opcion") 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        if miCola.limiteEspacios > 0:
            if anadir(miCola):
                print("El usuario ha sido añadido con éxtito")
        else:
            print("El parqueadero está lleno")
            
    elif opcion == 2:
        if not miCola.es_vacia():
            item = miCola.desencolar()
            print("El usuario, " + item.getNombre() + "ha sido desencolado")
        else:
            print("El parqueadero está vacio")
            
    elif opcion == 3:
        if not miCola.es_vacia():
            print("Usuarios:")
            miCola.mostrar()
        else:
            print("No hay usuarios en el parqueadero")
    
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 4")
    print()
    print('------------------------------------------')
print ("Fin")
