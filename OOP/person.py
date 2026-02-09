class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def greeting(self):
        print(f"Salom {self.firstName.title()}. Ahvollar qanday?")

    def __str__(self):
        return f"Bu obyektni print qilsa bo'ladi. return mavjed!!!"