#Hecho por Álvaro García Fernández 2ºC

nom=["dudi", "diego", "deivy", "elias", "luis"]             #Se crea una lista con 5 nombres
x=0
may5=0
while x<len(nom):                                           #Cuando que la longitud de la lista sea mayor que x
    if len(nom[x])>=5:                                      #Compara si la longitud de cada nombre es mayor que 5
        may5+=1                                             #Si lo es suma 1 a la cantidad de nombres con 5 o mas letras
    x=x+1
print("El número de nombres con 5 o mas letras son:", may5) #Imprime en pantalla la cantidad de nomnres con 5 o mas letras