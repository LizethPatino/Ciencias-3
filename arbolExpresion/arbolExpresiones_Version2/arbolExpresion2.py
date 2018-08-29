from pila import *
from arbol import *



def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-/*=":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)


def juntar_variables(valor, variable):
    tupla.append((variable, valor))      

def evaluar(arbol):
    op= "abc"
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor in op:
         for i in range(len(tupla)):
            if tupla[i][0] == arbol.valor:
                return tupla[i][1]
    if arbol.valor == "=":
        return juntar_variables(evaluar(arbol.izq), arbol.der.valor)
    return int(arbol.valor)

pila = Pila()


archivo = open("expresiones.in", "r")
archivo2=open("expresiones.out","w")
tupla =[]
lista = []

linea1 = archivo.readlines()

for linea2 in linea1:
    if len(linea2)>1:
        linea2= linea2[:-1]
        exp=linea2.split(" ")
        print(exp)
        convertir(exp, pila)
        evaluar(pila.desapilar())
        

for i in range(0,len(tupla)):
    archivo2.write(tupla[i][0]+"="+str(tupla[i][1])+"\n")

archivo.close()  
archivo2.close()
print (tupla)
