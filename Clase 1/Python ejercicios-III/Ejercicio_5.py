def CelciusAFahrenheit(grado):
    gradoFahrenheit=(grado*(9/5))+32
    return gradoFahrenheit

def CelciusAKelvin(grado):
    gradoKelvin=grado+273.15
    return gradoKelvin

opcion=int(input("Ingrese 1 si desea transformar de Celcius a Kelvin\nIngrese 2 si desea transformar de Celcius a Fahrenheit\nIngrese 0 para cortar\n"))

while(opcion!=0):
    if(opcion==1):
        grado=float(input("Ingrese la temperatura en Celcius\n"))
        print("Su temperatura en grados Kelvin es: ",CelciusAKelvin(grado))
    elif(opcion==2):
        gradoCelcius=float(input("Ingrese la temperatura en grados Fahrenheit\n"))
        print("La temoeratura en grados Fahrenheit es: ",CelciusAFahrenheit(gradoCelcius))
    else:
        print("Ingrese una opcion valida\n")

    opcion=int(input("Ingrese 1 si desea transformar de Celcius a Kelvin\nIngrese 2 si desea transformar de Celcius a Fahrenheit\nIngrese 0 para cortar\n"))
