gastoCliente=float(input("Ingrese cuanto dinero gasto el cliente\n"))
articulosComprados=float(input("Ingrese la cantidad de articulos comprados\n"))

if((gastoCliente>200)and(articulosComprados>2)):
    gastoCliente-=20
    print("El cliente tiene que pagar ",gastoCliente," pesos")
else:
    print("El cliente tiene que pagar ",gastoCliente," pesos")