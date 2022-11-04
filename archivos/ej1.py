paises = { 
    "pais1": {
        "id":"1",
        "nombre": "Argentina"
    },
    "pais2":{
       "id":"2",
       "nombre": "brasil" 
    }

}

#Agregando Paises

paisAAgregar=input("ingrese el numero del pais que desea agregar(0 para cortar)")

while paisAAgregar!="0":
    
    idAAgregar=input("ingrese el id del pais")
    nombreAAgregar=input("ingrese el nombre del pais")

    paises[paisAAgregar]={idAAgregar,nombreAAgregar}

    paisAAgregar=input("ingrese el numero del pais que desea agregar(0 para cortar")

print(paises)

#Borrando paises
paisABorrar=input("ingrese el numero del pais que desea borrar(0 para cortar)")

while paisABorrar!="0":
    
   del paises[paisABorrar]

   paisABorrar=input("ingrese el numero del pais que desea agregar(0 para cortar")

print(paises)        

