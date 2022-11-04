nota1=int(input("Ingrese la primera nota del estudiante\n"))
nota2=int(input("Ingrese la segunda nota del estudiante\n"))
nota3=int(input("Ingrese la tercera nota del estudiante\n"))

promedio = (nota1+nota2+nota3)/3
print(promedio)

if(promedio>=6):
    print("\nEl alumno aprobo")
else:
    print("\nEl alumno desaprobo")

