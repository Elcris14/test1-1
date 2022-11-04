import datetime

fechaActual = datetime.datetime.now()

opcion=int(input("ingrese 1 si quiere sumar dias\n ingrese 2 si desea restar dias\n ingrese 0 para cortar\n"))
while(opcion!=0):
    dias=int(input("ingrese a cantidad de dias\n"))

    if opcion == 1 :
        fechaResultante = fechaActual + datetime.timedelta(days=dias)
    elif opcion == 2:
        fechaResultante = fechaActual - datetime.timedelta(days=dias)
    else:
        print("ingrese una opcion valida\n")
    
    print("La fecha actual es",fechaActual)
    print("\nLa fecha resultante es",fechaResultante)
    
    opcion=int(input("ingrese 1 si quiere sumar dias\n ingrese 2 si desea restar dias\n ingrese 0 para cortar\n"))
