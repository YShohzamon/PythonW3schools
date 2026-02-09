class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print("Animal sound.")

    def sleep(self):
        print("Animal sleep.")

class Dog(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def time(self, distance):
        print(f"Dog spend {distance/self.speed} secund for {distance}m.")
class Cat(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def time(self, distance):
        print(f"{self.name} spends {distance/self.speed:.2f} secund for {distance}m.")
