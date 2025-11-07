### Public 
- by default all variables, method and class are considered as public access for python

### Private
- python don't have any specific syntax or modifier name to specify if object is private or not
- python has convention to specify private variables, you can still access that variable if you really want to
- in python you need to add double underscore as prefix to specify if object is private or not
- To access private variable you need to add `_ClassName` as prefix with variable name
```python
class MyClass:
    def __init__(self, value):
        self.__value = value

c = MyClass(10)
print(c._MyClass__value)
```
```
10
```

### Protected
- same as private variable only difference is that we only need to use single underscor `_` as prefix
- also you can directly access protected variable in python, unlike private 
- so in above code `c._name` will print protected variable

# Reference
- https://www.youtube.com/watch?v=43FK20rWvKQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=64
