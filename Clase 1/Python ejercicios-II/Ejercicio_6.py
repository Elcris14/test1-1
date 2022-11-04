gastoCliente=float(input("Ingrese cuanto dinero gasto el cliente\n"))
articulosComprados=float(input("Ingrese la cantidad de articulos comprados\n"))

if((gastoCliente>500)or(articulosComprados>3)):
    gastoCliente*=0.75
    print("El cliente tiene que pagar ",gastoCliente," pesos")
else:
    print("El cliente tiene que pagar ",gastoCliente," pesos")