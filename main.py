import json
import re
from country import Country

def insertDay(fileName, listOfCountries):
    # Expresion regular para evitar cuatrimestres
    p = re.compile('^20[\d][\d]$')
    for i in fileName["data"]:
        if (p.match(i["dimCodes"][1])):
            # ------- Pseudo funcion para buscar atributo de elemento -------------
            for country in listOfCountries:
                if country.isId(i["dimCodes"][0]):
                    country.numberOfDaysOfTourists.append(i["Valor"])
                    country.year.append(i["dimCodes"][1])
                    break

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

for index, name in enumerate(file1['categories'][0]['labels']):
    # Si el pais esta seleccionado:
    if name not in selected_countries: continue
    # Creo el objeto pais con ese nombre y un identifacdor
    auxObject = Country(name,file1["categories"][0]["codes"][index])
    # Se inserta en el vector de objetos paises
    listOfCountries.append(auxObject)

# Insertar media dias y año
insertDay(file1,listOfCountries)
    
#------------------------------------------------------------------------------------------
# Comprobar que todos los paises que hemos seleccionado estan en el fichero 1
file2["categories"][0]["labels"]
for i in selected_countries:
    assert i in file2["categories"][0]["labels"]

for index, name in enumerate(file2['categories'][0]['labels']):
    # Si el pais esta seleccionado:
    if name not in selected_countries: continue
    for country in listOfCountries:
        if country.name != name: continue
        country.id.append(file2["categories"][0]["codes"][index])
        break

insertDay(file2,listOfCountries)

for i in listOfCountries:
    print(i)
#------------------------------------------------------------------------------------------

# datos :
# nombre Alemania
# vector pair<año,n> estadistica (2018,9.34)

# objeto main:
# año
# vector paises
# datos par numero_medio_dias, inmigrantes