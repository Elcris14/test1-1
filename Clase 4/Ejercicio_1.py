import datetime

fechaActual = datetime.datetime.today()
print(fechaActual)

print("el año es",fechaActual.year)
print("el mes es",fechaActual.month)
semana=datetime.datetime.today().strftime("%W")
print("el numero de semana en el año es",semana)
print("el numero de dia es",fechaActual.day,"y es un",fechaActual.strftime("%A"))


