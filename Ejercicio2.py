#Hecho por Álvaro García Fernández 2ºC

num1=int(input("ingrese primer valor:"))    #ingresamos valores
num2=int(input("ingrese segundo valor:"))
if num1>num2:                               #comparamos valores
    suma=num1+num2                          #realizamos la suma y resta
    resta=num1-num2
    print("La suma es:",suma,"y la resta es:",resta)
else:
    producto=num1*num2                      #realizamos el producto y la division
    division=num1/num2
    print("El producto es:",producto,"y la division es:",division)