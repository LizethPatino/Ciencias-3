name "arreglo-mayor";ordenar arreglo de mayor a menor

org 100h;Indica que ensamble codigo a partir del offset 100h

mov cx, 8;# mover ->registro contador 8 

bucle1:

mov c, cx  ;variable c, copia el valor de cx
mov bx, cx ;bx-> registro base   
mov cx, 9  ;contador vectores (ordenar)

bucle2:   

mov si, cx ;Registro índice fuente
mov ah, v[si-1]; espacio de byte mas alto h - v:vector
cmp ah, v[bx-1]; comparar ah con la posicion bx-1 del vector

jnge seguir; condicional-si lo que hay en la posicion 8 en menor que la posicion 7
           ; no se hace nada y se ira directo a la etiqueta seguir
           ; sino se hara algoritmo de ordenacion       

mov dh,v[bx-1]  ; dx registro de datos (dh,dl)
mov dl, v[si-1]
mov v[bx-1], dl
mov v[si-1], dh  ;ordenar de mayor a menor

seguir: ; cuando no cumple condicional
loop bucle2
mov cx, c;reescribir decrementa 1

loop bucle1


ret

v db 2,32,64,32,8,121,5,21,91;sabe que es vector por medio de las comas
c dw 0;contador
