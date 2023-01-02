import json
import re
from country import Country

# Comprobar que todos los paises que hemos seleccionado estan en el fichero X
def assertCountries(fileName,countries):
    for i in countries:
        assert i in fileName["categories"][0]["labels"]

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

# Comprobar que todos los paises que hemos seleccionado estan en el fichero X
assertCountries(file1,selected_countries)

for index, name in enumerate(file1['categories'][0]['labels']):
    # Si el pais esta seleccionado:
    if name not in selected_countries: continue
    # Creo el objeto pais con ese nombre y un identifacdor
    auxObject = Country(name,file1["categories"][0]["codes"][index])
    # Se inserta en el vector de objetos paises
    listOfCountries.append(auxObject)

# Insertar media dias y año fichero 1
insertDay(file1,listOfCountries)
    
#------------------------------------------------------------------------------------------
assertCountries(file2,selected_countries)

for index, name in enumerate(file2['categories'][0]['labels']):
    # Si el pais esta seleccionado:
    if name not in selected_countries: continue
    for country in listOfCountries:
        if country.name != name: continue
        country.id.append(file2["categories"][0]["codes"][index])
        break

# Insertar media dias y año fichero 2
insertDay(file2,listOfCountries)

# Numero medio de turistas 2021-2010 ok
# -----------------------------------------------------------------------------

# Lectura fichero 3
file3 = None
with open('file5.json') as jsonFile:
    file3 = json.load(jsonFile)

lowestYear = int(min(listOfCountries[0].year))
biggestYear = int(max(listOfCountries[0].year))

for i in file3["data"]:
    for country in listOfCountries:
        if not country.isId(i["dimCodes"][0]): continue
        if (lowestYear <= int(i["dimCodes"][1]) <= biggestYear) and (i["dimCodes"][2] == "T"):
            #print("Valor:", i["Valor"], "Pais:", i["dimCodes"][0], "Año:",  i["dimCodes"][1], "Sexo:", i["dimCodes"][2])
            country.numberOfInmigrants.append(i["Valor"])
            break

for i in listOfCountries:
    print(i)

