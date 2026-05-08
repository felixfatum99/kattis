index_getter = {
    "Skrimsli":{
        "Skrimsli":0,
        "Venjulegt":1,
        "Ahrifa":2,
        "Bodunar":3,
        "Samruna":4,
        "Samstillt":5,
        "Thaeo":6,
        "Penduls":7,
        "Tengis":8},
    "Galdur":{
        "Galdur":9,
        "Venjulegur":10,
        "Bunadar":11,
        "Svida":12,
        "Samfelldur":13,
        "Bodunar":14,
        "Hradur":15},
    "Gildra":{
        "Gildra":16,
        "Venjuleg":17,
        "Samfelld":18,
        "Mot":19},
    "Annad":{
        "Annad":20
    }
}

sorting = {
    "nafn":0, 
    "id":1, 
    "flokkur":2,
    "dagsetning":3
}

l = []

N = int(input())

for _ in range(N):
    name, id, type, date = input().split(", ")

    type2 = type

    if "-" in type:
        types = type.split(" - ")
        type = types[0]
        type2 = types[1]
    
    year, month, day = date.split("-")
    l.append((name, id, index_getter[type][type2], int(year), int(month), int(day)))

sort_strategy = []
sort = input().split()
for t in sort:
    index = sorting[t]
    sort_strategy.append(index)
    if index == 3:
        sort_strategy.append(4)
        sort_strategy.append(5)


list = sorted(l, key=lambda element: (element[sort_strategy[0]], element[sort_strategy[1]], element[sort_strategy[2]], element[sort_strategy[3]], element[sort_strategy[4]], element[sort_strategy[5]]))
for item in list:
    print(item[0])
