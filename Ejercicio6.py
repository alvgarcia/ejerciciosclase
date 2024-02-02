#Hecho por Álvaro García Fernández 2ºC

n=int(input("Introducir número de pares de datos:"))            #Incializar valores y variables
b=0
h=0
a=0
cantidad=0
for f in range(n):                                              #introducir la base y altura y ensañar en pantalla y calacular la superficie y comparar si es mayor que 12
    b=int(input("Introducir base:"))
    h=int(input("Introducir altura:"))
    a=b*h/2
    print("La base es:",b)
    print("La altura es:",h)
    print("El área es:",a)
    if a>12:
        cantidad+=1
print("La cantidad de triángulos con superficie mayor que 12 es:",cantidad)         #Imprimir la cantidad de triánguloscon superficie mayores de 12