def CelciusAFahrenheit(grado):
    gradoFahrenheit=(grado*(9/5))+32
    return gradoFahrenheit

gradoCelcius=float(input("Ingrese la temperatura en grados Celcius\n"))

print("La temoeratura en grados Fahrenheit es: ",CelciusAFahrenheit(gradoCelcius))