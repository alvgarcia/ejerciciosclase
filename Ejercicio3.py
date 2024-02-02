# Álvaro García Fernández 2ºC

nºpreg=int(input("Ingrese número total de preguntas:"))    #se ingresan el nº de preguntas y de ciertos
nºcorr=int(input("Ingrese número de aciertos:"))
por=nºcorr/nºpreg*100                                      #se realiza el porcentaje
if por>=90:                                                #se realiza 
    print("Has obtenido el nivel máximo.")
elif por>=75:
    print("Has obtenido el nivel medio.")
elif por>=50:
    print("Has obtenido el nivel regular.")
else:
    print("Estas fuera de nivel.")