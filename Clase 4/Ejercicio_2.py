
def anioBisiesto(anio):
    if (anio%4==0) and ((anio%100!=0) or (anio%400==0)):
        print("El año",anio,"es bisiesto")
    else:
        print("El año",anio,"no es bisiesto")

anio=int(input("Ingrese el año para saber si es bisiesto o no\n"))

anioBisiesto(anio)