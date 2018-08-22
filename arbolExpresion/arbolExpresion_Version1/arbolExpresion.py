from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)
    
#exp = input("ingrese l expresion en posfija: ").split(" ")

pila = Pila()

#convertir(exp, pila)

#print (evaluar(pila.desapilar()))

archivo = open("expresionesin.txt", "r")
archivo2 = open("expresionesout.txt", "w")
linea1 = archivo.readlines()
lista = []
for linea2 in linea1:
    if len(linea2)>1:
        linea2= linea2[:-1]
        exp=linea2.split(" ")
        print(exp)
        convertir(exp, pila)
        #print (evaluar(pila.desapilar()))
        resultado = evaluar(pila.desapilar())
        archivo2.write(str(resultado) + '\n') 






archivo.close()
archivo2.close()
