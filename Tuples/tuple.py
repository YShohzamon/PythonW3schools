fruits = ("olma", "anor", "uzum", "behi", "gilos")
cars = ("BMW", "Mers", "Lacetti", "Malibu", "Nexia")
numbers = (1,2,3,4,5,5,6,7,8,9,9,4,6,73,12,34,6,3,565,43,75,23,65,32,67,76,100,32)
names = ('alisher', 'bobur', 'sherzod', 'doston', 'behruz','sherzod' , 'ruslan', 'ozod', 'bobur')
emptyList = tuple()

print(type(fruits))

# tuple ga malumot qo'shish usuli
x = list(fruits)
print(type(x))

# fruits.append("ananas") #ishlamaydi
x.append("ananas")
fruits = tuple(x)
print(fruits)

emptyList =cars + fruits + numbers
print(emptyList)

def numberCount(n):
    return f"Ro'yxatdagi {n}lar soni: {numbers.count(n)}"

counts = list()
for num in numbers:
    counts.append(numbers.count(num))

print(counts)
print(f"Minumum: {min(counts)}, maximum: {max(counts)}, O'rtacha: {sum(counts)/len(counts)}")
print(counts.count(max(counts)))
print(counts.count(min(counts)))

print("Yetarli!!!")








