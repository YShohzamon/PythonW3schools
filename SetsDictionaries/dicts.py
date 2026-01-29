myDictionary = {
    1:{
        "name": "shohzamon",
        "age": 20,
        "height": 170,
        "weight": 56,
        "job": "AI engineer",
        "programming_language": ["Python", "C++", "JavaScript"],
        "lang": ["uzbek", "english"]
    },
    2:{
        "name": "ozodbek",
        "age": 22,
        "height": 175,
        "weight": 60,
        "job": "Web developer",
        "programming_language": ["Python", "JavaScript", "Php"],
        "lang": ["uzbek", "english", "russian"]
    }
}

for x in myDictionary.values():
    print(x)

for x in myDictionary.items():
    print(x)

for x in myDictionary.keys():
    print(x)

print(f"{myDictionary[1]["name"]} {len(myDictionary[1]['lang'])} ta tilni biladi!")
print(f"{myDictionary[1]["name"]} {len(myDictionary[1]['programming_language'])} ta dasturlash tilini biladi!")

for x, obj in myDictionary.items():
    for y in obj:
        print(f"{y}: {myDictionary[x][y]}")