#Hecho por Álvaro García Fernández 2ºC

lisma=[]
lista=[]
for f in range (4):                                     #Se crea un bucle para introducir los sueldos de los empleados de la mañana
    suema=int(input("Ingrese un sueldo:"))
    lisma.append(suema)
for x in range (4):                                     #Se crea otro bucle para introducir los sueldos de los empleados de la tarde
    sueta=int(input("Ingrese un sueldo:"))
    lista.append(sueta)
print("Los sueldos del turno de mañana son:", lisma)    #Se imprimen en pantalla las dos listas
print("Los sueldos del turno de tarde son:", lista)