#Hecho por Álvaro García Fernández 2ºC

name1=input("Ingrese el primer nombre:")            #Ingresamos los nombres en las variables
name2=input("Ingrese el segundo nombre:")
while name1==name2:                                 #Hasta que no se ingresen dos nombres distintos no pasa a la comparacion
    name2=input("Ingrese un nombre distinto:")
if name1<name2:                                     #Se comparan los nombres y el que vaya primero alfabeticamente se escribe primero
    print(name1,name2)
else:
    print(name2,name1)