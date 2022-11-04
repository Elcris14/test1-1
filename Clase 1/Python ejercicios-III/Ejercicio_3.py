def CelciusAKelvin(grado):
    gradoKelvin=grado+273.15
    return gradoKelvin

grado=float(input("Ingrese la temperatura en grados celcius\n"))
print("Su temperatura en grados Kelvin es: ",CelciusAKelvin(grado))
