# Álvaro García Fernández 2ºC

cantidad=0                                                                                      #Definimos las variables y se las asigna un valor
n=int(input("Cuantos valores ingresará:"))
for f in range(n):                                                                              #Se introducen n números definidos en la variable n y se detecta si son mayores o iguales a mil
    valor=int(input("Ingrese el valor:"))
    if valor>=1000:
        cantidad+=1                                                                             #Se le suma uno a la varible que almacena el número de números mayores o iguales a mil
print("La cantidad de valores ingresados mayores o igual a mil es:",cantidad)                   #Se imprime en la pantalla la cantidad de números