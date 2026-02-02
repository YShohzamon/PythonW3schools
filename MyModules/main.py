import myFunctions
import platform
from myFunctions import personData

print(dir(myFunctions)) # ichida bor funksiyalarni ko'rsatadi.
myFunctions.greating('Shohzamon')
mylist  = "sasks;ffwef qwefowife woeif qweofiwe wq;kfwqfejlsfiqwe fiw efwioeldfwqefijasfj"
print(myFunctions.findLength(mylist))

x = platform.system()
print(x)

files = dir(platform)
print(files)
print(platform.__version__)

print(f"{personData['name']} {personData['age']} yosh.")
