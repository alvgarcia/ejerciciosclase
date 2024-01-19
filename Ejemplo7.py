#Hecho por Álvaro García Fernández 2ºC

opcion="si"                                                 #Definimos y damos valor a las variables
suma=0
while opcion=="si":                                         #Mientras opcion sea si se seguiran ingresando mas valores
    valor=int(input("Ingrese un valor:"))                   #Ingresa la variable y se suma al total y se elige si se quiere ingresar otro numero
    suma+=valor
    opcion=input("Desea cargar otro numero (si/no):")
print("La suma de valores ingresados es:",suma)             #Se imprime en pantalla la suma de los numeros introducidos