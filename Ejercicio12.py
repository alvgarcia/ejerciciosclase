#Hecho por Álvaro García Fernández 2ºC

lis=[]
x=0
for f in range(5):                      #Creamos un bucle para ingresar los valoresde la lista
    n=int(input("Ingrese un valor:"))
    lis.append(n)
print(lis)                            #Se imprime en pantalla la lista
while x<len(lis):                       #Se crea un bucle para eliminar los num mayores a 10 comparandolo uno a uno
    if lis[x]>=10:
        lis.pop(x)
    else:
        x+=1
print(lis)
