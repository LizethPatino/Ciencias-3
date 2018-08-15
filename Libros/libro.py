from cola import *

cola = Cola()

def mostrarBusqueda(lista):
    print(" Los Libros actuales: ")
    for item in lista:
        print("* {}".format(item))
    print("")

def buscar(criterio, valor_busqueda):
    cola_resultados = Cola()
    for item in cola.items:
        if valor_busqueda == item[criterio]:
            cola_resultados.encolar(item)
    mostrarBusqueda(cola_resultados.items)

def run():
    
    OPCIONES = "1) Ingresar un libro \n2) Busqueda de libros por género\n3) Busqueda de libros  por autor\n4) Busqueda de libros  por nombre\n5) Ver todos los libros"
    while True:
        opcion = int(input("Selecciona el número de la opción para la consulta: \n{}:\n".format(OPCIONES)))
        
        if opcion == 1:
            print("\tIngresar un libro\n")
            nombre = input("Nombre del libro: ")
            autor = input("Autor del libro: ")
            genero = input("Género del libro: ")
            libro = {
                'Nombre': nombre,
                'Autor': autor,
                'Genero': genero
            }
            cola.encolar(libro)
            
        elif opcion == 2:
            print("\t Busqueda de libros por género")
            gen_buscar = input("Ingrese la búsqueda: ")
            buscar('Genero',gen_buscar)
            
        elif opcion == 3:
            print("\tBusqueda de libros por autor")
            gen_buscar = input("Ingrese la búsqueda: ")
            buscar('Autor',gen_buscar)

        elif opcion == 4:
            print("\tBusqueda de libros por nombre")
            gen_buscar = input("Ingrese la búsqueda: ")
            buscar('Nombre',gen_buscar)
        elif opcion == 5:
            mostrarBusqueda(cola.items)
        else:
            print("Opcion no valida... ")
    
    
if __name__ == '__main__':
    run()
