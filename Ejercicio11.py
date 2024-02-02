#Hecho por Álvaro García Fernández 2ºC

lis=[]
for f in range(5):                                      #Creamos un bucle para poner en la lista 5 num enteros
    num=int(input("Ingrese un numero entero:"))
    lis.append(num)
may=0
repe=0
a=0
for x in range (len(lis)):                              #Con un bucle comparamos los num de la lista
    if lis[x]==may:                                     #Si el mayor es igual al num seleccionado la var repe se suma 1
        repe+=1 
    if lis[x]>may:                                      #Si el num selecionado la var may se iguala a la seleccion y el num de num repetidos se iguala a 1
        repe=1
        may=lis[x]
print("La lista es:", lis)                              #Se imprime en pantalla La lista y el num mayor
print("El numero mayor es:", may)
if repe>1:                                              #Si el num se repite mas de una vez se imprime la primera string y si no la segunda
    print("El numero mayor aparece:", repe, "veces")
else:
    print("El numero mayor aparece:", repe, "vez")