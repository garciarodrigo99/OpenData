import json

def find(lista, elemento):
    if  elemento in lista:
        return True
    return False

data = None
with open('file1.json') as jsonFile:
    d = json.load(jsonFile)


selected_countries = ["Alemania","Bélgica","Francia","Holanda","Irlanda","Italia","Reino Unido","Suiza"]
select_id = []

d["categories"][0]["labels"]
for i in selected_countries:
    assert i in d["categories"][0]["labels"]
    
for i in selected_countries:
    select_id
    
print(selected_countries)

#print(d["categories"][0]["labels"][1])

# print(data)

# datos :
# nombre Alemania
# vector pair<año,n> estadistica (2018,9.34)

# objeto main:
# año
# vector paises
# datos par numero_medio_dias, inmigrantes