import json
import re
from country import Country

c1 = Country("Alemania")

# Lectura fichero 1
file1 = None
with open('file1.json') as jsonFile:
    file1 = json.load(jsonFile)

# Lectura fichero 2
file2 = None
with open('file3.json') as jsonFile:
    file2 = json.load(jsonFile)

#------------------------------------------------------------------------------
# Declaración paises que queremos incluir
selected_countries = ["Alemania","Bélgica","Francia","Holanda","Irlanda","Italia","Reino Unido","Suiza"]
id_selected_countries = []
listOfObjects = []
#------------------------------------------------------------------------------

# Comprobar que todos los paises que hemos seleccionado estan en el fichero 1
file1["categories"][0]["labels"]
for i in selected_countries:
    assert i in file1["categories"][0]["labels"]

sizeOfCountries = len(file1["categories"][0]["labels"]) # Obtener size

for i in range(sizeOfCountries):    # Recorro labels por su indice
    # Si el pais esta seleccionado:
    if file1["categories"][0]["labels"][i] in selected_countries:
        # Propuesta de eliminacion
        id_selected_countries.append(file1["categories"][0]["codes"][i])
        # Creo el objeto pais con ese nombre
        auxObject = Country(file1["categories"][0]["labels"][i])
        # Añado ese id al objeto
        auxObject.id.append(file1["categories"][0]["codes"][i])
        auxObject.id.append(f'{i}')
        print(auxObject.name, end=" ")
        print(auxObject.sizeId(), end= " ")
        # Se inserta en el vector de objetos paises
        listOfObjects.append(auxObject)
        print(len(listOfObjects))
        for i in listOfObjects:
            print(i.name, end=" ")
            print(i.id)

# Expresion regular para evitar cuatrimestres
p = re.compile('^20[\d][\d]$')

for i in file1["data"]:
    #if (p.match(i["dimCodes"][1])) and (i["dimCodes"][0] in id_selected_countries):
    if (p.match(i["dimCodes"][1])):
        found = False
        # ------- Pseudo funcion para buscar atributo de elemento -------------
        listofobjetsSize = len(listOfObjects)
        #print("\n-----------------------Empieza for j-----------------------")
        for j in range(listofobjetsSize):
            #print(i["dimCodes"][0], end=" ")
            #print(listOfObjects[j].name)
            ##print("Numero de ids: ",end=" ")
            ##print(listOfObjects.)
            if listOfObjects[j].isId(i["dimCodes"][0]):
                found = True
                break
        # ---------------------------------------------------------------------
        if found == True:
            print("País: "+i["dimCodes"][0]+"\tValor: "+i["Valor"]+"\tAño: "+i["dimCodes"][1])
#------------------------------------------------------------------------------------------
file2["categories"][0]["labels"]
for i in selected_countries:
    assert i in file2["categories"][0]["labels"]

sizeOfCountries = len(file2["categories"][0]["labels"])
for i in range(sizeOfCountries):
    if file2["categories"][0]["labels"][i] in selected_countries:
        id_selected_countries.append(file2["categories"][0]["codes"][i])

for i in file2["data"]:
    #if (p.match(i["dimCodes"][1])) and (i["dimCodes"][0] in id_selected_countries):
    if (p.match(i["dimCodes"][1])):
        for j in listOfObjects:
            if i["dimCodes"][0] in j.id:
                print("País: "+i["dimCodes"][0]+"\tValor: "+i["Valor"]+"\tAño: "+i["dimCodes"][1])
#------------------------------------------------------------------------------------------
# for i in listOfObjects:
#     print(i.name)

#print(d["categories"][0]["labels"][1])

# datos :
# nombre Alemania
# vector pair<año,n> estadistica (2018,9.34)

# objeto main:
# año
# vector paises
# datos par numero_medio_dias, inmigrantes