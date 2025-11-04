---
title: Class
---
### Basic
```python
class Math:
    def sum(number1,number2):
        return number1+number2
    
a=10
b=20
print(Math.sum(a,b))
```
### Class with properties
```python
class Person:
    Name=""
    Age=""

    def PrintData(self):
        print(f"Name:{self.Name}")
        print(f"Age:{self.Age}")
    
p= Person()
p.Name="Vivek"
p.Age=31;

p.PrintData()
```
### Class with static method
```python
class Person:
    Name=""
    Age=""

    def __init__(self,name,age):
        print("New person class created")
        self.Name=name
        self.Age=age
    
    @staticmethod
    def SayHello():
        print("Hello Sir")


p= Person("Vivek",31)
Person.SayHello()
```
### Class with constructor
- Python can have only one constructor, so if you create multiple method with `__init__` python will only use last one
```python
class Person:
    Name=""
    Age=""

    def __init__(self,name,age):
        print("New person class created")
        self.Name=name
        self.Age=age

    def PrintData(self):
        print(f"Name:{self.Name}")
        print(f"Age:{self.Age}")
    

p= Person("Vivek",31)
p.PrintData()
```
- To use multiple instructor use classmethod decorator
```python
class Person:
    Name: (str)
    Age: (int)

    def __init__(self):
        self.Name = "Vivek"
        self.Age = 31
        print("New person class created")

    @classmethod
    def from_name(cls, name):
        person = cls()
        person.Name = name
        person.Age = 31
        return person

    @classmethod
    def from_name_age(cls, name, age):
        person = cls()
        person.Name = name
        person.Age = age
        return person

    def __str__(self):
        return f"Hey my name is {self.Name}. I am {self.Age} year old"


p = Person()
print(p)

p = Person.from_name("Vivek")
print(p)

p = Person.from_name_age("Vivek", 31)
print(p)

```
### Class with getter and setter
```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property  # Getter
    def value(self):
        return self._value*10

    @value.setter # Setter
    def value(self, new_value):
        self._value = new_value/10


c = MyClass(10)
print(c.value)
c.value = 1000
print(c._value)
print(c.value)
```
### Class with inheritance
```python
class Person:
    Name=""
    Age=""

    def __init__(self):
        print("New person class created")
        
    def __init__(self,name,age):
        print("New person class created")
        self.Name=name
        self.Age=age

    def PrintData(self):
        print(f"Name:{self.Name}")
        print(f"Age:{self.Age}")
    

class Employee(Person):
    Salary=10000
    Company="Microsoft"

    def PrintData(self):
        super().PrintData()
        print(f"Age:{self.Company}")
        print(f"Age:{self.Salary}")

p= Employee("Vivek",31)
p.PrintData()

```
### Create list using custom class
```python
class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # method to calculate distance from origin
    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # method to calculate distance from another point
    def distance_from_point(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    # method to print the point coordinates
    def __str__(self):
        return f"({self.x}, {self.y})"


# creating list of point
points = []

for i in range(1, 11):
    point = Point(i, 2*i)
    points.append(point)

for point in points:
    print(point)
```
