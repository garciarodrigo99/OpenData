import json

for file in ['file1.json', 'file3.json', 'file5.json']:
  with open(file, 'r') as jsonFile:
    file1 = json.load(jsonFile)
    json.dump(file1, open(file, 'w'), indent=4)