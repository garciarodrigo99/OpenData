import json
import re
from country import Country

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
listOfCountries = []
#------------------------------------------------------------------------------

# Comprobar que todos los paises que hemos seleccionado estan en el fichero 1
file1["categories"][0]["labels"]
for i in selected_countries:
    assert i in file1["categories"][0]["labels"]

sizeOfCountries = len(file1["categories"][0]["labels"]) # Obtener size

for index, name in enumerate(file1['categories'][0]['labels']):
    # Si el pais esta seleccionado:
    if name not in selected_countries: continue
    # Creo el objeto pais con ese nombre y un identifacdor
    auxObject = Country(name,file1["categories"][0]["codes"][index])
    # Se inserta en el vector de objetos paises
    listOfCountries.append(auxObject)

# Expresion regular para evitar cuatrimestres
p = re.compile('^20[\d][\d]$')

for i in file1["data"]:
    if (p.match(i["dimCodes"][1])):
        # ------- Pseudo funcion para buscar atributo de elemento -------------
        for country in listOfCountries:
            if country.isId(i["dimCodes"][0]):
                country.numberOfDaysOfTourists.append(i["Valor"])
                country.year.append(i["dimCodes"][1])
                break

for i in listOfCountries:
    print(i)
    
#------------------------------------------------------------------------------------------
file2["categories"][0]["labels"]
for i in selected_countries:
    assert i in file2["categories"][0]["labels"]

for i in file2["data"]:
    #if (p.match(i["dimCodes"][1])) and (i["dimCodes"][0] in id_selected_countries):
    if (p.match(i["dimCodes"][1])):
        for j in listOfCountries:
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