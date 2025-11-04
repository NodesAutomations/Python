---
title: Module
---
### Check for main module
```python
class MyClass:
    def __init__(self, value):
        self._value = value


if __name__ == "__main__":
    c = MyClass(10)
    print(c._value)
```
- In python we normally start typeing code directly below any class or functions
- this normally works when you have only single python file
- But this will create problem when you have multiple python files, importing each other
- so if i import this module in another file , code below my class will automatically gets executated, which is not desired behavirour
- so to avoid this issue we add this main check using if, so only when we are directly running this specific file this code will get executed
