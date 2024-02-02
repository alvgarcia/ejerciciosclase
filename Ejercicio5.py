# Álvaro García Fernández 2ºC

n=int(input("Ingrese el número de números enteros que quiera introducir:"))         #defino las varibles y las doy un valor
x=1
par=0
impar=0
while x<=n:                                                                         #se introduce el número y se detecta si es par o impar y se le suma a una variable para llevar el recuento
    valor=int(input("Ingrese el número entero:"))
    if valor%2==0:
        par+=1
    else:
        impar+=1
    x+=1
print("ELnúmero de pares es:",par,"y el de impares es:",impar)                      #se imprime el número de números impares y pares