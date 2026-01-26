fruits = ["olma", "anor", "uzum", "behi", "gilos"]
cars = ["BMW", "Mers", "Lacetti", "Malibu", "Nexia"]
numbers = [1,2,3,4,5,5,6,7,8,9,9,4,6,73,12,34,6,3,565,43,75,23,65,32,67,76,100,32]
names = ['alisher', 'bobur', 'sherzod', 'doston', 'behruz','sherzod' , 'ruslan', 'ozod', 'bobur']
emptyList = list()

[emptyList.append(x) for x in numbers if x>23]
print("Bosh listni to'ldirish:")
print(emptyList)

print("Bo'shlistni tartiblash:")
emptyList.sort()
print(emptyList)

print("200 ga nisbatan yaqinlik bo'yicha tartiblash")
def nearSort(n):
    return abs(n-200)

emptyList.sort(key=nearSort)
print(emptyList)

print("Listga son qo'shish va olib tashlash va bo'shatish va o'chirib tashlash")
print(emptyList)
emptyList.insert(5, "Bye")
emptyList.append("oxiridaman!")
emptyList.pop(3)
emptyList.remove(565)
print(emptyList, "endi bo'shatamiz.")
emptyList.clear()
print(emptyList)
# del emptyList
# print(emptyList) to'liq o'chirib tashlandi!

print("__________Mashinalar")
for car in cars:
    print(car)

print("_____________ismlar:")
i = 0
while i < len(names):
    print(names[i])
    i = i + 1

