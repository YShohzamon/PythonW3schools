from person import Person
from animals import *

p1 = Person("shohzamon", "yaqubov")
p1.greeting()

p2 = Person("alibek", "Ganiyev")
p2.greeting()

del p2
try:
    p2.greeting()
except NameError:
    print("Obyekt topilmadi. Iltimos tekshiring!!!")

p3 = Person("ada", "asda")
print(p3)
print("----------------Animals------------------")

a1 = Animal("cat", 3)
a1.sound()
a1.sleep()

cat1 = Cat("Mosh", 3, 11.2)
cat1.time(120)
cat1.sleep()
cat1.sound()