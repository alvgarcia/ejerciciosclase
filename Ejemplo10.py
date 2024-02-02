#Hecho por Álvaro García Fernández 2ºC

lista=[]
valor=int(input("Ingresar valor (0 para finalizar):"))
while valor!=0:
    lista.append(valor)
    valor=int(input("Ingresar valor (0 para finalizar):"))
print("Tamaño de la lista:",len(lista))