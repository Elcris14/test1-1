
class BankAccount():
    def __init__(self,numeroDeCuenta,nombre,saldo):
        self.numeroDeCuenta=numeroDeCuenta
        self.nombre=nombre
        self.saldo=saldo

    def deposito(self,montoADepositar):
        self.saldo=self.saldo+montoADepositar

    def retiro(self,montoARetirar):
        if(montoARetirar<=self.saldo):
            self.saldo=self.saldo-montoARetirar
        else:
            print("No dispone de fondos suficientes")

    def comisionBancaria(self):
        self.saldo=self.saldo*0.95

    def display(self):
        print("La cuenta bancaria de ", self.numeroDeCuenta," posee un nombre de: ", self.nombre, " con un saldo de: ", self.saldo)


persona1 = BankAccount(1,"rodrigo",10000)
persona1.deposito(2000)
persona1.retiro(10000)
persona1.display()



