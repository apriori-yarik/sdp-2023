# ООП

## Създаване на клас с конструктор и атрибути

```python
class Human:
		# class attribute
    counter = 0

    def __init__(self, name, age, egn):
        self.name = name
        self.age = age

				# частен атрибут
				self.__egn = egn

        Human.counter += 1

human1 = Human("Ivan", 20)
human2 = Human("Pesho", 30)

print(human1.name, human1.age) # Ivan 20
print(human2.name, human2.age) # Pesho 30
print(Human.counter) # 2
```

## hasattr, getattr, setattr

```python
print(hasattr(human1, "name")) # True
print(hasattr(human1, "ag")) # False

print(getattr(human1, "name")) # Ivan

setattr(human1, "age", 50)
print(human1.age) # 50
```

## Методи за извеждане - “__str__”, “__repr__”

```python
class Human:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Human.counter += 1
		
		# __repr__ => аналогичен метод
    def __str__(self):
        return f"{self.name} is {self.age} years old"

human1 = Human("Ivan", 20)
human2 = Human("Pesho", 30)

print(human1) # Ivan is 20 years old
```

## Class and static methods

```python
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

human1 = Human("Ivan", 20, "0000000000")
human2 = Human("Pesho", 30, "1111111111")

print(Human.counter) # 2
Human.reset_counter()
print(Human.counter) # 0

print(Human.isAdult(human1)) # True
```

## property()

```python
class Human:
    counter = 0

    def __init__(self, name, age, egn):
        self.name = name
        self.age = age
        self.__egn = egn
        Human.counter += 1
    
    def get_egn(self):
        return self.__egn
    
    def set_egn(self, egn):
        self.__egn = egn

    egn = property(get_egn, set_egn)

human1 = Human("Ivan", 20, "0000000000")
human2 = Human("Pesho", 30, "1111111111")

print(human1.egn) # 0000000000
human1.egn = "0123456789"
print(human1.egn) # 0123456789
```

## Декоратор property()

```python
class Human:
    counter = 0

    def __init__(self, name, age, egn):
        self.name = name
        self.age = age
        self.__egn = egn
        Human.counter += 1

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    @property
    def egn(self):
        return self.__egn
    
    @egn.setter
    def egn(self, egn):
        self.__egn = egn

human1 = Human("Ivan", 20, "0000000000")
human2 = Human("Pesho", 30, "1111111111")

print(human1.egn)
human1.egn = "0123456789"
print(human1.egn)
```

## Наследяване

```python
class Student(Human):
    def __init__(self, name, age, egn, school):
        super().__init__(name, age, egn)
        self.school = school

student1 = Student("Anna", 18, "2222222222", "some school")
print(student1.name, student1.school) # Anna some school
```

## Полиморфизъм

```python
class Human:
    counter = 0

    def __init__(self, name, age, egn):
        self.name = name
        self.age = age
        self.__egn = egn
        Human.counter += 1

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    @property
    def egn(self):
        return self.__egn

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

student = Student("Anna", 18, "2222222222", "some school")
teacher = Teacher("Georgi", 40, "3333333333", "some school")

people = [student, teacher]
for i in people:
    print(i.do()) # в зависимост от типа на обекта i резултатът ще бъде различен
```
