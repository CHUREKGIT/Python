sentense = "Ala ma kota, kot ma Ale"
list_of_worlds = sentense.split(" ")

for i in list_of_worlds:
    if ',' in i:
        list_of_worlds[list_of_worlds.index(i)] = i[:-1]

print(list_of_worlds)