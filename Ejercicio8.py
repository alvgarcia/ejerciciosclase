#Hecho por Álvaro García Fernández 2ºC

password=input("Ingrese una contaseña entre 10 y 20 caracteres:")            #Se introduce la contraseña que se guarda en una variable de caracteres
if len(password)>=10 and len(password)<=20:           #Se comprueba que la contraseña sea de la longitud indicada y se imprime si se guarda o error depepndiendo de la longitud
    print("Guardada")
else:
    print("Error")