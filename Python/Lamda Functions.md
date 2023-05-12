### Overview
- Lamda function is a small anonymous functions without name

### Sample code
```python
square=lambda x:x*x
cube=lambda x:x*x*x

print(square(5)) # Prints 25
print(cube(5)) # Prints 125
```
### function with multiple variables
```python
avg=lambda x,y,z:(x+y+z)/3

print(avg(1,2,3)) # print 2
```
### function as input paramter
```python
def Test(fx, value):
    return 5+fx(value)

print(Test(lambda x: x*x, 5))  # prints 30
print(Test(lambda x: x*x*x, 5))  # prints 130
```

