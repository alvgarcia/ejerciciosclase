# Álvaro García Fernández 2ºC

cantidad=0                                                  #defino las variables necesarias y las doy un valor
x=1
n=int(input("Cuantas piezas cargara:"))
while x<=n:                                                 #Se ingresan las medidas de las piezas y se cuantan las que valen
    largo=float(input("Ingrese la medida de las pieza:"))
    if largo>=1.2 and largo<=1.3:
        cantidad+=1
    x+=1
print("La cantidad de piezas aptas son:",cantidad)           #Se imprime en pantalla las piezas aptas