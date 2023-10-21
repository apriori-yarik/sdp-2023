class Human:
    counter = 0

    def __init__(self, name, age, egn):
        self.name = name
        self.age = age
        self.__egn = egn
        Human.counter += 1

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    @classmethod
    def reset_counter(cls):
        cls.counter = 0

    @staticmethod
    def isAdult(human):
        return human.age > 18
    
    @property
    def egn(self):
        return self.__egn
    
    @egn.setter
    def egn(self, egn):
        self.__egn = egn

    # def get_egn(self):
    #     return self.__egn
    
    # def set_egn(self, egn):
    #     self.__egn = egn

    # egn = property(get_egn, set_egn)

    def do():
        return None

class Student(Human):
    def __init__(self, name, age, egn, school):
        super().__init__(name, age, egn)
        self.school = school

    def do(self):
        return "Homework"
    
class Teacher(Human):
    def __init__(self, name, age, egn, school):
        super().__init__(name, age, egn)
        self.school = school

    def do(self):
        return "Teach students"

human1 = Human("Ivan", 20, "0000000000")
human2 = Human("Pesho", 30, "1111111111")

print(Human.counter)
Human.reset_counter()
print(Human.counter)

print(Human.isAdult(human1))

print(hasattr(human1, "name"))
print(hasattr(human1, "ag"))

print(getattr(human1, "name"))

setattr(human1, "age", 50)
print(human1.age)

print(human1)

print(human1.egn)
human1.egn = "0123456789"
print(human1.egn)

print("---------------------")

student1 = Student("Anna", 18, "2222222222", "some school")
print(student1.name, student1.school)

teacher = Teacher("Georgi", 40, "3333333333", "some school")

people = [student1, teacher]
for i in people:
    print(i.do())