#Hecho por Álvaro García Fernández 2ºC

lista=[]
for x in range(10):
    val=int(input("Ingrese valor:"))
    lista.append(val)
print(lista)
posi=0
while posi<len(lista):
    if lista[posi]==5:
        lista.pop(posi)
    else:
        posi+=1
print(lista)