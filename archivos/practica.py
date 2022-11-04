print("1 si desea sumar")
print("2 si desea restar")
print("3 si desea dividir")
print("4 si desea multiplicar")
a=int(input("ingrese un numero o 0 para cortar"))
while(a!=0):
    match a:
        case 1:
            b=float(input("ingrese el primer numero "))
            c=float(input("ingrese el segundo numero "))
            suma=b+c
            print(suma)
        case 2:
            b=float(input("ingrese el primer numero "))
            c=float(input("ingrese el segundo numero "))
            resta=b-c
            print(resta)
        case 3:
            b=float(input("ingrese el primer numero "))
            c=float(input("ingrese el segundo numero "))
            producto=b*c
            print(producto)
        case 4:
            b=float(input("ingrese el primer numero "))
            c=float(input("ingrese el segundo numero "))
            if c!=0:
                division=b/c
                print(division)
            else:
                print("Ingrese un valor distinto de 0 para el cociente")
        case other:
            print("ingrese un numero entre 1 y 4")
    a=int(input("ingrese un numero o 0 para salir de la app"))

    



