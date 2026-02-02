for i in range(10):
    print(chr(i+97)) # kichik harflar.

myString = "Hello World!"
myList = list()
for x in myString:
    myList.append(x)

print(myList)

i = 0
while i < len(myList):
    print(myList[i])
    i = i + 1