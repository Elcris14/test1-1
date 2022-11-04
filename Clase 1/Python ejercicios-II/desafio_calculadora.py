opcion=int(input("Ingrese la opcion a realizar:\n 1) si desea sumar\n 2) si desea restar\n 3)si desea multiplicar\n 4)si desea dividir\n0)para cortar\n"))

while(opcion!=0):

    numero1=float(input("Ingrese el primer numero\n"))
    numero2=float(input("Ingrese el segundo numero\n"))

    if(opcion==1):
        operacion=numero1+numero2
        print("La suma es ", operacion)
    elif(opcion==2):
        operacion=numero1-numero2
        print("La resta es ", operacion)
    elif(opcion==3):
        operacion=numero1*numero2
        print("La multiplicacion es ", operacion)
    elif(opcion==4):
        if(numero2!=0):
            operacion=numero1/numero2
            print("La division es ", operacion)
        else:
            print("No se puede dividir por 0")
    else:
        print("No ha ingresado un numero entre 1 y 4\n")

    opcion=int(input("Ingrese la opcion a realizar:\n 1) si desea sumar\n 2) si desea restar\n 3)si desea multiplicar\n 4)si desea dividir\n0)para cortar\n"))
