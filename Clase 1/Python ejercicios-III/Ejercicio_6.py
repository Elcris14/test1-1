def ParOImpar(numero):
    if((numero%2)==0):
        print("El numero",numero,"es par\n")
    else:
        print("El numero",numero,"es impar\n")

numero=int(input("Ingrese el numero\n"))

ParOImpar(numero)