# Álvaro García Fernández 2ºC

num1=int(input("Ingrese primer número:"))    #se ingresan los números
num2=int(input("Ingrese segunda número:"))
num3=int(input("Ingrese tercer número:"))
if num1>num2 and num1>num3:                    #se comparan los números y se elige el mayor
    print("El mayor de los tres es:",num1)
elif num2>num3:
    print("El mayor de los tres es:",num2)
else:
    print("El mayor de los tres es:",num3)