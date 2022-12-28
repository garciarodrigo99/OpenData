import json
import re

data = None
with open('file1.json') as jsonFile:
    d = json.load(jsonFile)

#------------------------------------------------------------------------------
selected_countries = ["Alemania","Bélgica","Francia","Holanda","Irlanda","Italia","Reino Unido","Suiza"]
id_selected_countries = []

d["categories"][0]["labels"]
for i in selected_countries:
    assert i in d["categories"][0]["labels"]

sizeOfCountries = len(d["categories"][0]["labels"])
for i in range(sizeOfCountries):
    if d["categories"][0]["labels"][i] in selected_countries:
        id_selected_countries.append(d["categories"][0]["codes"][i])

p = re.compile('^20[\d][\d]$')
for i in d["data"]:
    if (p.match(i["dimCodes"][1])) and (i["dimCodes"][0] in id_selected_countries):
        print("País: "+i["dimCodes"][0]+"\tValor: "+i["Valor"]+"\tAño: "+i["dimCodes"][1])

#------------------------------------------------------------------------------

#print(d["categories"][0]["labels"][1])

# print(data)

# datos :
# nombre Alemania
# vector pair<año,n> estadistica (2018,9.34)

# objeto main:
# año
# vector paises
# datos par numero_medio_dias, inmigrantes