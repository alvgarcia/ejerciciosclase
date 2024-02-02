# Álvaro García Fernández 2ºC

nota1=int(input("Ingrese primer nota:"))    #se ingresan las notas
nota2=int(input("Ingrese segunda nota:"))
nota3=int(input("Ingrese tercer nota:"))
prom=(nota1+nota2+nota3)/3                  #se realiza el promedio y se compara para ver que mensaje poner
if prom>=7:
    print("Promocionado")
elif prom>=4:
    print("Regular")
else:
    print("Reprobado")