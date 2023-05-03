### Function without return
```python
def PrintNumber(i):
    print(f"Number is {i}")

# print number 1-10
for i in range(1,11):
    PrintNumber(i)
```
### function with return
```python
def factor(number):
    value=1
    while number>1:
        value=value*number
        number=number-1
    return value

print(factor(3))
```

### function with default parameter value
```python
def factor(number=2):
    value=1
    while number>1:
        value=value*number
        number=number-1
    return value

print(factor())
```

### Function with recursion
```python
def factor(number):
    value=1
    if (number==0 or number==1):
        return value
    else :
        value=number*factor(number-1);
    return value

for i in range(6):
    print(factor(i))
```