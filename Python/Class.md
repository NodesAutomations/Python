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
    
    @staticmethod
    def SayHello():
        print("Hello")

p= Person()
p.Name="Vivek"
p.Age=31;

p.PrintData()
p.SayHello()
```

### Class with constructor
- Python can have only one constructor, so if you create multiple method with `__init__` python will only use last one
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
    

p= Person("Vivek",31)
p.PrintData()
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
