import json
import re

file1 = None
with open('file1.json') as jsonFile:
    file1 = json.load(jsonFile)

file2 = None
with open('file3.json') as jsonFile:
    file2 = json.load(jsonFile)

#------------------------------------------------------------------------------
selected_countries = ["Alemania","Bélgica","Francia","Holanda","Irlanda","Italia","Reino Unido","Suiza"]
id_selected_countries = []
#------------------------------------------------------------------------------
file1["categories"][0]["labels"]
for i in selected_countries:
    assert i in file1["categories"][0]["labels"]

sizeOfCountries = len(file1["categories"][0]["labels"])
for i in range(sizeOfCountries):
    if file1["categories"][0]["labels"][i] in selected_countries:
        id_selected_countries.append(file1["categories"][0]["codes"][i])

p = re.compile('^20[\d][\d]$')
for i in file1["data"]:
    if (p.match(i["dimCodes"][1])) and (i["dimCodes"][0] in id_selected_countries):
        print("País: "+i["dimCodes"][0]+"\tValor: "+i["Valor"]+"\tAño: "+i["dimCodes"][1])
#------------------------------------------------------------------------------------------
file2["categories"][0]["labels"]
for i in selected_countries:
    assert i in file2["categories"][0]["labels"]

sizeOfCountries = len(file2["categories"][0]["labels"])
for i in range(sizeOfCountries):
    if file2["categories"][0]["labels"][i] in selected_countries:
        id_selected_countries.append(file2["categories"][0]["codes"][i])

p = re.compile('^20[\d][\d]$')
for i in file2["data"]:
    if (p.match(i["dimCodes"][1])) and (i["dimCodes"][0] in id_selected_countries):
        print("País: "+i["dimCodes"][0]+"\tValor: "+i["Valor"]+"\tAño: "+i["dimCodes"][1])
#------------------------------------------------------------------------------------------


#print(d["categories"][0]["labels"][1])

# datos :
# nombre Alemania
# vector pair<año,n> estadistica (2018,9.34)

# objeto main:
# año
# vector paises
# datos par numero_medio_dias, inmigrantes