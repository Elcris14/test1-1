import json

archivo=open("poke.json","r")
textop=archivo.read()
listaP=json.loads(textop)

for pokemon in listaP:
    if pokemon["#"] == 54:
        print(pokemon)


