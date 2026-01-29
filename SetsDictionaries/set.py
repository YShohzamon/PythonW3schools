mySet = {1, 3 , 4 , 'apple', 'banana', 'apple', False, True, 0}
mySet2 = {False, 'banana', 'bmw', 'mers', 1}
print(len(mySet))
print("----------------------")
for x in mySet:
    print(x)

mySet.add("Bobur")
print(mySet)

print("----------------------")
#birlashma
print(mySet.union(mySet2))
print(mySet | mySet2)

#keshishma
print(mySet.intersection(mySet2))
print(mySet & mySet2)

#ayirma
print(mySet.difference(mySet2))
print(mySet - mySet2)

#simmetrik ayirma
print(mySet.symmetric_difference(mySet2))