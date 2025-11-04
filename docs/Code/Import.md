---
title: Import
parent: Code
---

### Import Entire module
- Importing in python is process of loading code from a python module into the current script
- This allows you to use the functions and variables defined in the module in your current script also any additional modules that the imported module might depend upon
- For example to import the math module
```python
import math

result=math.sqrt(9)
print(result) # output : 3.0
```

### Import specific function
```python
form math import sqrt

result=math.sqrt(9)
print(result) # output : 3.0
```
for multiple functions use comma 
```python
form math import sqrt,pi
```

### import using as keywork
```python
import math as m

result=m.sqrt(9)
print(result) # output : 3.0
```

### Use Modules or class from multiple file
person.py
```python
class Person:
    Name=""
    Age=""

    def PrintData(self):
        print(f"Name:{self.Name}")
        print(f"Age:{self.Age}")
```
mainfile
```python
from Person import Person

p= Person()
p.Name="Vivek"
p.Age=31
p.PrintData();
```
### Import Modules from sub folder
sub folder file : Util/Calculator.py
```python
class Calculator:
    def sum(number1,number2):
        return number1+number2
```
main file
```python
from Util.Calculator import Calculator
a=10
b=20
print(Calculator.sum(a,b))
```
### Use Specific version of package
ref : [Force python to use older version of package](https://stackoverflow.com/questions/6445167/force-python-to-use-an-older-version-of-module-than-what-i-have-installed-now)
```python
import pkg_resources
pkg_resources.require("Twisted==8.2.0")
import twisted
```
or
```python
__requires__= 'twisted==8.2.0'
import pkg_resources
pkg_resources.require("twisted==8.2.0")
import twisted  
```